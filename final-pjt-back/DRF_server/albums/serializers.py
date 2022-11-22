from rest_framework import serializers
from .models import Album


# class AlbumIdSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Album
#         fields = ('id',)


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = (
<<<<<<< HEAD
            'content',
=======
            'user',
            'review',
>>>>>>> upstream/master
        )


# class ReviewContentSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Review
#         fields = ('content',)


class AlbumListSerializer(serializers.ModelSerializer):
    # review = ReviewSerializer(many=True, read_only=True)

    class Meta:
        model = Album
        fields = '__all__'
        read_only_fields = ('review',)


class AlbumSerializer(serializers.ModelSerializer):
    # review = ReviewSerializer(many=True, read_only=True)

    class Meta:
        model = Album
        fields = '__all__'
        read_only_fields = ('review',)
