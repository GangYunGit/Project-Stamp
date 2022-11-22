from rest_framework import serializers
from .models import Album, Review


# class AlbumIdSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Album
#         fields = ('id',)


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = (
            'album',
            'content',
        )
        read_only_fields = ('album',)


class ReviewContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ('content',)


class AlbumListSerializer(serializers.ModelSerializer):
    review = ReviewSerializer(many=True)

    class Meta:
        model = Album
        fields = '__all__'
        read_only_fields = ('review',)


class AlbumSerializer(serializers.ModelSerializer):
    review = ReviewContentSerializer(many=True)

    class Meta:
        model = Album
        fields = '__all__'
        read_only_fields = ('review',)
