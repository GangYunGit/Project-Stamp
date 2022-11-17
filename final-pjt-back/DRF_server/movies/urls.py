from django.urls import path
from . import views

app_name='movies'

urlpatterns = [
    # path('actors/', views.actor_list),
    # path('actors/<int:actor_pk>/', views.actor_detail),
    path('', views.movie_list),
    path('<int:movie_pk>/', views.movie_detail),
    path('genres/', views.genre_list),
    path('actors/', views.actor_list),
    path('genres/index', views.genre_index, name='index'),
    path('genres/<int:genre_pk>/like/', views.like_genre),
    # path('reviews/', views.review_list),
    # path('reviews/<int:review_pk>/', views.review_detail),
    # path('movies/<int:movie_pk>/reviews/', views.create_review),
]