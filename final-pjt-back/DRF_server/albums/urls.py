from django.urls import path
from . import views

app_name = 'albums'

urlpatterns = [
    path('', views.album_index),
    path('<int:album_pk>/', views.album_detail),
    path('<int:album_pk>/review/', views.review_create),
]
