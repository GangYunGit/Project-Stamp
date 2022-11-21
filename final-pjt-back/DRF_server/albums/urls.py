from django.urls import path
from . import views

app_name = 'albums'

urlpatterns = [
    path('', views.album_index),
    path('<int:album_pk>/', views.album_detail),
    path('<int:album_pk>/review/<int:review_pk>/', views.review),
    path('<int:album_pk>/review_create/', views.review_create),
]
