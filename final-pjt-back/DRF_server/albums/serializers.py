from rest_framework import serializers
from .models import Album


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = (
            'user',
            'review',
        )


class AlbumListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = '__all__'
        read_only_fields = ('review',)


class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = '__all__'
        read_only_fields = ('review',)
