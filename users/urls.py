"""Defines URL patterns for users"""

from django.urls import path, include

app_name = 'users'
urlpatterns = [
    # Include default auth url
    path('', include('django.contrib.auth.urls')),

]