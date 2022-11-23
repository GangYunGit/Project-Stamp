from django.urls import path
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from . import views

# swagger 사용하려면 app_name을 잠깐 주석처리하고 사용
app_name = 'movies'

urlpatterns = [
    path('', views.movie_list),
    path('<int:movie_pk>/', views.movie_detail),
    path('genres/', views.genre_list),
    path('actors/', views.actor_list),
    path('user/likes/', views.user_likes),
    path('recommendation/<int:user_pk>/', views.recommendation),
    # swagger urls
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path(
        'swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'
    ),
]
