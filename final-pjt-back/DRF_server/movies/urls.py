from django.urls import path
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from . import views

# swagger 사용하려면 app_name을 잠깐 주석처리하고 사용!
app_name = 'movies'

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
    # 필수 작성
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    # optional UI
    path(
        'swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'
    ),
]
