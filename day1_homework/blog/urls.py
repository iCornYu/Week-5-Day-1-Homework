from django.urls import path

from . import views

urlpatterns = [
    path('index/', views.index, name = 'blog-index'),
    path('', views.homePage, name = 'blog-home')
]