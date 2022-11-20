from django.db import models
from django.conf import settings

class Album(models.Model):
    movie_title = models.CharField(max_length=100)
    movie_poster_path = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    review = models.TextField()
    # user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
