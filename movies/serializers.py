from rest_framework import serializers
from .models import Movie, Genre,Review
from django.contrib.auth import get_user_model

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'

class MovieSerializer(serializers.ModelSerializer):
    genres = GenreSerializer(many=True, read_only=True)
    class Meta:
        model = Movie
        fields = '__all__'

class ReviewSerializer(serializers.ModelSerializer):
    class UserSerializer(serializers.ModelSerializer):
        password = serializers.CharField(write_only=True)
        class Meta:
            model = get_user_model()
            fields = ('username','password',)

    user = UserSerializer(read_only=True)
    movie = MovieSerializer(read_only=True)

    class Meta:
        model = Review
        fields = '__all__'


