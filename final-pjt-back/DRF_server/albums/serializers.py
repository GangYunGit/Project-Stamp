from rest_framework import serializers
from .models import Album, Review


class AlbumIdSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = ('id',)


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'
        read_only_fields = ('album',)


class ReviewContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ('content',)


class AlbumListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = (
            'user',
            'movie_title',
            'movie_poster_path',
            'review',
        )
        read_only_fields = ('review',)


class AlbumSerializer(serializers.ModelSerializer):
    # review = ReviewSerializer(read_only=True)

    class Meta:
        model = Album
        fields = ('user', 'movie_title', 'movie_poster_path', 'review')
