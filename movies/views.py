from django.shortcuts import render
from rest_framework.response import Response
from .models import Movie
from .serializers import MovieSerializer
from rest_framework import status
from rest_framework.decorators import api_view

# Create your views here.
@api_view(['GET'])
def get_movies(request):
    if request.method == 'GET':

        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data)
