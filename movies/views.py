from django.shortcuts import get_object_or_404, render
from django.template import response
from rest_framework.response import Response
from .models import Movie, Review
from .serializers import MovieSerializer,ReviewSerializer
from rest_framework import serializers, status
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import AllowAny

# Create your views here.
@api_view(['GET'])
@permission_classes([AllowAny])
def get_movies(request):
    if request.method == 'GET':
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data)

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
def delete_reviews(request,detail_id,review_id):
    if request.method == 'DELETE':
        review = get_object_or_404(Review,pk = review_id)
        review.delete()
        return Response({'review_id':review_id},status=status.HTTP_204_NO_CONTENT
        )


