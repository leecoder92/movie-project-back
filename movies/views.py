from django.shortcuts import render
from rest_framework.response import Response
from .models import Movie
from .serializers import MovieSerializer

# Create your views here.
def get_movies(request):
    movies = Movie.objects.all()
    serializer = MovieSerializer(movies, many=True)
    return Response(serializer.data)