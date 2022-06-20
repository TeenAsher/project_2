"""Defines URL patterns for kisik"""

from django.urls import path

from . import views

app_name = 'cat'
urlpatterns = [
    # Home page
    path('', views.index, name='index'),
    # Path that shows all topics
    path('topics/', views.topics, name='topics')
]