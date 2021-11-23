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