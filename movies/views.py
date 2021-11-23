from typing import ItemsView
from django.shortcuts import get_object_or_404, render
from django.template import response
from rest_framework.response import Response
from .models import Movie, Review
from .serializers import MovieSerializer,ReviewSerializer
from rest_framework import serializers, status
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import AllowAny
from operator import attrgetter

# Create your views here.
@api_view(['GET'])
@permission_classes([AllowAny])
def get_movies(request):
    if request.method == 'GET':
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data)

# ================================================================

@api_view(['GET', 'POST'])
@permission_classes([AllowAny])
def get_reviews(request,detail_id):
    if request.method == 'GET':
        reviews = Review.objects.filter(movie_id=detail_id).all()
        # reviews=request.user.review_set.all()
        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ReviewSerializer(data=request.data)
        movie = get_object_or_404(Movie,pk=detail_id)
        print(movie)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user,movie=movie)
            return Response(serializer.data,status=status.HTTP_201_CREATED)


@api_view(['DELETE'])
def delete_reviews(request, detail_id, review_id):
    if request.method == 'DELETE':
        review = get_object_or_404(Review,pk = review_id)
        review.delete()
        return Response({'review_id':review_id},status=status.HTTP_204_NO_CONTENT
        )

# =============================================================================================

# 영화데이터 내의 평점과 사람들이 직접 남긴 평점의 평균을 비교, 직접 남긴 평점이 높은 영화들을 추천
@api_view(['GET'])
def recommend(request):
    if request.method == 'GET':
        movies = Movie.objects.all()
        recommend_list = []
        for movie in movies:
            review_avg_list = []
            reviews = Review.objects.filter(movie_id=movie.id).all()
            for review in reviews:
                review_avg_list.append(float(review.rank))

            if review_avg_list:
                review_avg = sum(review_avg_list)/len(review_avg_list)
            else:
                review_avg = 0

            if (movie.vote_average >= 6.0 and review_avg>=3.0) and (movie.vote_average<=review_avg*2):
                recommend_list.append(movie)

        recommend_list = sorted(recommend_list,key=attrgetter('vote_average'),reverse=True)
        if len(recommend_list)>10:
            new_list=[]
            for new in recommend_list[10]:
                new_list.append(new)
            recommend_list = new_list
        serializer = MovieSerializer(recommend_list,many=True)
        return Response(serializer.data)


# 로그인한 사람이 평점을 4점 이상으로 남긴 영화들의 장르를 모아서 비슷한 장르의 영화를 추천
@api_view(['GET'])
def recommendv2(request):
    genre_set = set()
    movies = Movie.objects.all()
    recommend_set = set()
    recommend_list = []
    reviews = request.user.review_set.all()
    for review in reviews:
        if review.rank >= 4:
            movie = Movie.objects.filter(pk=review.movie_id)[0]
            genres = movie.genres.all()
            for genre in genres:
                genre_set.add(genre)
    for genre in genre_set:
        for movie in movies:
            if genre in movie.genres.all() and movie.vote_average >= 4:
                recommend_set.add(movie)
    for movie in recommend_set:
        recommend_list.append(movie)
    recommend_list.sort(key=lambda movie: movie.vote_average, reverse=True)
    recommend_list = recommend_list[:10]
    
    serializer = MovieSerializer(recommend_list, many=True)
    return Response(serializer.data)