from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('newsletter/', views.news_letter, name='news_letter'),
    path('privacy/', views.privacy_policy, name='privacy'),
]
