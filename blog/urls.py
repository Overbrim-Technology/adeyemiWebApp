from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog, name='blog'),
    path('<str:category>-<str:datetime>-<str:slug>/', views.article, name='article'),
]
