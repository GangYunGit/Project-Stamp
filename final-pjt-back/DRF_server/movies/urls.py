from django.urls import path
from . import views

app_name='movies'

urlpatterns = [

    path('', views.movie_list),
    path('<int:movie_pk>/', views.movie_detail),
    path('genres/', views.genre_list),
    path('actors/', views.actor_list),
    path('like_genres/', views.genre_index, name='like_genres'),
    path('genres/<int:genre_pk>/like/', views.like_genre),
    path('actors/<int:actor_pk>/like/', views.like_actor),
    path('<int:movie_pk>/like/', views.like_movie),
    path('user_likes/', views.user_likes, name='user_likes'),
    path('users/', views.users),
    path('recommendation/<int:user_pk>/', views.recommendation),

]