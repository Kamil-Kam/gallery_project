from django.urls import path
from . import views

urlpatterns = [
    path('gallery/<str:category_name>/', views.gallery, name='gallery'),
    path('photo/<str:category>/<str:pk>/', views.photo, name='photo'),
    path('add_photo/', views.add_photo, name='add_photo'),
    path('', views.main_website, name='main'),
    path('milky_way_carousel<str:active>/<str:next_photo>/<str:next_next_photo>/', views.milky_way_carousel, name='milky_way_carousel'),
    path('see_photo/<str:the_photo>/', views.see_photo, name='see_photo'),
]
