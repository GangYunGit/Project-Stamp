from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_list_or_404, get_object_or_404, render, redirect
from django.http import JsonResponse

from .models import Album
from .serializers import AlbumListSerializer, AlbumSerializer, ReviewSerializer


@api_view(['GET', 'POST'])
def album_index(request):
    # 테스트용 앨범 리스트 전체 보여주는 view함수(GET 만)
    if request.method == 'GET':
        albums = get_list_or_404(Album)
        serializer = AlbumListSerializer(albums, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = AlbumListSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def album_detail(request, album_pk):
    album = get_object_or_404(Album, pk=album_pk)
    if request.method == 'GET':
        serializer = AlbumSerializer(album)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = AlbumSerializer(album, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

    elif request.method == 'DELETE':
        album.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def review(request, album_pk, review_pk):
    review = get_object_or_404(Album, pk=review_pk)
    serializer = ReviewSerializer(review)
    return Response(serializer.data)


@api_view(['PUT'])
def review_create(request, album_pk):
    album = get_object_or_404(Album, pk=album_pk)
    serializer = ReviewSerializer(album, data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
