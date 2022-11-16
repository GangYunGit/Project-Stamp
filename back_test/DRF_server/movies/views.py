from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.shortcuts import get_list_or_404, get_object_or_404

from .serialzers import MovieListSerializer, MovieSerializer
from .models import Movie


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
