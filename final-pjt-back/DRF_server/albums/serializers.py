from rest_framework import serializers
from .models import Album


class AlbumListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Album
        fields = ('movie_title', 'movie_poster_path')


class AlbumSerializer(serializers.ModelSerializer):

    class Meta:
        model = Album
        fields = '__all__'