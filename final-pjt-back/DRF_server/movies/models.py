from django.db import models
from django.conf import settings


class Genre(models.Model):
    name = models.CharField(max_length=50)
    like_users = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name='like_genres',
    )


class Movie(models.Model):
    genre_ids = models.ManyToManyField(Genre, null=True)
    overview = models.TextField(null=True)
    poster_path = models.TextField(null=True)
    release_date = models.DateTimeField(null=True)
    title = models.CharField(null=True, max_length=100)
    vote_average = models.FloatField(null=True)
    vote_count = models.IntegerField(null=True)
    like_users = models.ManyToManyField(
        settings.AUTH_USER_MODEL, related_name='like_movies'
    )


class Actor(models.Model):
    name = models.TextField()
    movie_ids = models.ManyToManyField(Movie)
    profile_path = models.TextField(null=True)
    like_users = models.ManyToManyField(
        settings.AUTH_USER_MODEL, related_name='like_actors'
    )
