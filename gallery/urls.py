from django.urls import path
from . import views

urlpatterns = [
    path('gallery/<str:category_name>/', views.gallery, name='gallery'),
    path('photo/<str:category>/<str:pk>/', views.photo, name='photo'),
    path('add_photo/', views.add_photo, name='add_photo'),
    path('', views.main_website, name='main'),
]
