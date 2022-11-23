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
        fields = ('id', 'name', 'like_users')


class GenreLikeUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = (
            'id',
            'like_genres',
        )
        read_only_fields = ('id',)


class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = (
            'id',
            'name',
        )


class ActorLikeUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = (
            'id',
            'like_actors',
        )
        read_only_fields = ('id',)


class UserLikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = (
            'id',
            'like_genres',
            'like_actors',
        )
        read_only_fields = ('id',)


class RecommendationSerializer(serializers.ModelSerializer):
    user = get_user_model()
    like_movies = MovieSerializer(many=True)

    class Meta:
        model = get_user_model()
        fields = ('like_movies',)
