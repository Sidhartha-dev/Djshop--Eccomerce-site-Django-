from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='blogHome'),
    path('blogPost/', views.blogpost, name='blogPost'),
]
