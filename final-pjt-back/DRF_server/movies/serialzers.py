from rest_framework import serializers
from .models import Movie, Genre, Actor
from django.contrib.auth import get_user_model


# class ActorSerializer(serializers.ModelSerializer):
#     movies = MovieTitleSerializer(many=True)

#     class Meta:
#         model = Actor
#         fields = ('id', 'movies', 'name')


# class ActorNameSerializer(serializers.ModelSerializer):
    
#     class Meta:
#         model = Actor
#         fields = ('name',)


# class ReviewSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = Review
#         fields = ('title', 'content',)

class MovieListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = ('title', 'overview', 'poster_path')


class MovieTitleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = ('title',)


class MovieSerializer(serializers.ModelSerializer):
    # actors = ActorNameSerializer(many=True)
    # review_set = ReviewSerializer(many=True)

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

# class ReviewDetailSerializer(serializers.ModelSerializer):
#     movie = MovieTitleSerializer(read_only=True)

#     class Meta:
#         model = Review
#         fields = ('id', 'movie', 'title', 'content')
