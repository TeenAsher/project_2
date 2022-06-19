"""Defines URL patterns for kisik"""

from django.urls import path

from . import views

app_name = 'cat'
urlpatterns = [
    # Home page
    path('', views.index, name='index'),
]