from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from django.contrib.auth import get_user_model
from django.shortcuts import get_list_or_404, get_object_or_404
from django.http import JsonResponse

from .serialzers import (
    MovieListSerializer,
    MovieSerializer,
    GenreSerializer,
    GenreLikeUserSerializer,
    UserLikesSerializer,
    ActorListSerializer,
    RecommendationSerializer,
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
    serializer = ActorListSerializer(actors, many=True)
    return Response(serializer.data)


# def genre_index(request):
#     genres = Genre.objects.all()
#     context = {
#         'genres': genres,
#     }
#     return render(request, 'movies/genre_index.html', context)


@api_view(['GET', 'PUT'])
@permission_classes([IsAuthenticated])
def like_genre(request):
    # if request.user.is_authenticated:
    # genre = get_object_or_404(Genre)
    # if genre.like_users.filter(pk=request.user.pk).exists():
    #     genre.like_users.remove(request.user)
    # else:
    #     genre.like_users.add(request.user)
    user = request.user
    if request.method == 'GET':
        serializer = GenreLikeUserSerializer(user)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = GenreLikeUserSerializer(instance=user, data=request.data)
        print(serializer)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            print(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    # return redirect('accounts:login')


def like_actor(request, actor_pk):
    # if request.user.is_authenticated:
    actor = Actor.objects.get(pk=actor_pk)

    if actor.like_users.filter(pk=request.user.pk).exists():
        actor.like_users.remove(request.user)
        is_liked = False
    else:
        actor.like_users.add(request.user)
        is_liked = True
    context = {
        'is_liked': is_liked,
    }
    return JsonResponse(context)
    # return redirect('accounts:login')


def like_movie(request, movie_pk):
    # if request.user.is_authenticated:
    movie = Movie.objects.get(pk=movie_pk)

    if movie.like_users.filter(pk=request.user.pk).exists():
        movie.like_users.remove(request.user)
        is_liked = False
    else:
        movie.like_users.add(request.user)
        is_liked = True
    context = {
        'is_liked': is_liked,
    }
    return JsonResponse(context)
    # return redirect('accounts:login')


# def user_likes(request):
#     genres = Genre.objects.all()
#     movies = Movie.objects.all()
#     actors = Actor.objects.all()
#     context = {
#         'genres': genres,
#         'movies': movies,
#         'actors': actors,
#     }
#     return render(request, 'movies/user_likes.html', context)


@api_view(['GET'])
def users(request):
    users = get_user_model().objects.all()
    serializer = UserLikesSerializer(users, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def recommendation(request, user_pk):
    genres = Genre.objects.filter(like_users=user_pk)
    movie = Movie.objects.distinct().filter(genre_ids__in=genres).order_by('?')[:20]
    serializer = MovieSerializer(movie)
    return Response(serializer.data)
