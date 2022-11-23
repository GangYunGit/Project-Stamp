from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from django.contrib.auth import get_user_model
from django.shortcuts import get_list_or_404, get_object_or_404
from django.http import JsonResponse
from django.db.models import Q

from .serialzers import (
    MovieListSerializer,
    MovieSerializer,
    GenreSerializer,
    ActorSerializer,
    # ActorLikeUserSerializer,
    # GenreLikeUserSerializer,
    UserLikeSerializer,
)
from .models import Movie, Genre, Actor


@api_view(['GET'])
def movie_list(request):
    movies = get_list_or_404(Movie)
    serializer = MovieListSerializer(movies, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def movie_detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    serializer = MovieSerializer(movie)
    return Response(serializer.data)


@api_view(['GET'])
def genre_list(request):
    genres = get_list_or_404(Genre)
    serializer = GenreSerializer(genres, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def actor_list(request):
    actors = get_list_or_404(Actor)
    serializer = ActorSerializer(actors, many=True)
    return Response(serializer.data)


# @api_view(['GET', 'PUT'])
# @permission_classes([IsAuthenticated])
# def like_genre(request):
#     user = request.user
#     if request.method == 'GET':
#         serializer = GenreLikeUserSerializer(user)
#         return Response(serializer.data)

#     elif request.method == 'PUT':
#         serializer = GenreLikeUserSerializer(instance=user, data=request.data)
#         print(serializer)
#         if serializer.is_valid(raise_exception=True):
#             serializer.save()
#             print(serializer)
#         return Response(serializer.data, status=status.HTTP_201_CREATED)


# @api_view(['GET', 'PUT'])
# @permission_classes([IsAuthenticated])
# def like_actor(request):
#     user = request.user
#     if request.method == 'GET':
#         serializer = ActorLikeUserSerializer(user)
#         return Response(serializer.data)

#     elif request.method == 'PUT':
#         serializer = ActorLikeUserSerializer(instance=user, data=request.data)
#         print(serializer)
#         if serializer.is_valid(raise_exception=True):
#             serializer.save()
#             print(serializer)
#         return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT'])
@permission_classes([IsAuthenticated])
def user_likes(request):
    user = request.user
    if request.method == 'GET':
        serializer = UserLikeSerializer(user)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = UserLikeSerializer(instance=user, data=request.data)
        print(serializer)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            print(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def recommendation(request, user_pk):
    genres = Genre.objects.filter(like_users=user_pk)
    actors = Actor.objects.filter(like_users=user_pk)
    print(genres)
    print(actors)
    movie = (
        Movie.objects.distinct()
        .filter(Q(genre_ids__in=genres) | Q(actor__in=actors))
        .order_by('?')[:20]
    )
    serializer = MovieSerializer(movie, many=True)
    return Response(serializer.data)
