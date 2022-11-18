from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.contrib.auth import get_user_model
from django.shortcuts import get_list_or_404, get_object_or_404, render, redirect
from django.http import JsonResponse

from .serialzers import MovieListSerializer, MovieSerializer, GenreSerializer, UserLikesSerializer, ActorListSerializer
from .models import Movie, Genre, Actor


# @api_view(['GET'])
# def actor_list(request):
#     actors = get_list_or_404(Actor)
#     serializer = ActorListSerializer(actors, many=True)
#     return Response(serializer.data)


# @api_view(['GET'])
# def actor_detail(request, actor_pk):
#     actor = get_object_or_404(Actor, pk=actor_pk)
#     serializer = ActorSerializer(actor)
#     return Response(serializer.data)


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


def genre_index(request):
    genres = Genre.objects.all()
    context = {
        'genres': genres,
    }
    return render(request, 'movies/genre_index.html', context)



# 포스트 요청으로 장르 ID 아무거나 주소에 파라미터로 넘겨서 주면??
def like_genre(request, genre_pk):
    if request.user.is_authenticated:
        genre = Genre.objects.get(pk=genre_pk)

        if genre.like_users.filter(pk=request.user.pk).exists():
            genre.like_users.remove(request.user)
            is_liked = False
        else:
            genre.like_users.add(request.user)
            is_liked = True
        context = {
            'is_liked': is_liked,
        }
        return JsonResponse(context)
    return redirect('accounts:login')


def like_actor(request, actor_pk):
    if request.user.is_authenticated:
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
    return redirect('accounts:login')


def like_movie(request, movie_pk):
    if request.user.is_authenticated:
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
    return redirect('accounts:login')


def user_likes(request):
    genres = Genre.objects.all()
    movies = Movie.objects.all()
    actors = Actor.objects.all()
    context = {
        'genres': genres,
        'movies': movies,
        'actors': actors,
    }
    return render(request, 'movies/user_likes.html', context)

@api_view(['GET'])
def users(request):
    users = get_user_model().objects.all()
    serializer = UserLikesSerializer(users, many=True)
    return Response(serializer.data)

# @api_view(['GET'])
# def review_list(request):
#     reviews = get_list_or_404(Review)
#     serializer = ReviewSerializer(reviews, many=True)
#     return Response(serializer.data)


# @api_view(['GET', 'DELETE', 'PUT'])
# def review_detail(request, review_pk):
#     review = get_object_or_404(Review, pk=review_pk)
#     if request.method == 'GET':
#         serializer = ReviewDetailSerializer(review)
#         return Response(serializer.data)

#     elif request.method == 'DELETE':
#         deleted_review_pk = review_pk
#         review.delete()
#         delete_message = f'review {deleted_review_pk} is deleted'
#         context = {
#             'delete': delete_message,
#         }
#         return Response(context, status=status.HTTP_204_NO_CONTENT)

#     elif request.method == 'PUT':
#         serializer = ReviewDetailSerializer(review, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)


# @api_view(['POST'])
# def create_review(request, movie_pk):
#     movie = get_object_or_404(Movie, pk=movie_pk)
#     serialzer = ReviewSerializer(data=request.data)
#     if serialzer.is_valid(raise_exception=True):
#         serialzer.save(movie=movie)
#         return Response(serialzer.data, status=status.HTTP_201_CREATED)
