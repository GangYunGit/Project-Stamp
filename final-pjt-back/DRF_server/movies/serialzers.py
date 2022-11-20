from rest_framework import serializers
from .models import Movie, Genre, Actor
from django.contrib.auth import get_user_model


class MovieListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = ('id', 'title', 'overview', 'poster_path')


class MovieSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = '__all__'


class GenreSerializer(serializers.ModelSerializer):

    class Meta:
        model = Genre
        fields = ('id', 'name',)


class ActorListSerializer(serializers.ModelSerializer):

    class Meta:
            model = Actor
            fields = '__all__'


class ActorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Actor
        fields = ('name', 'profile_path')


class UserLikesSerializer(serializers.ModelSerializer):
    like_genres = GenreSerializer(many=True)
    like_actors = ActorSerializer(many=True)
    like_movies = MovieSerializer(many=True)

    class Meta:
        model = get_user_model()
        fields = ('email', 'like_genres', 'like_actors', 'like_movies',)


class RecommendationSerializer(serializers.ModelSerializer):
    user = get_user_model()
    like_movies = MovieSerializer(many=True)

    class Meta:
        model = get_user_model()
        fields = ('like_movies',)