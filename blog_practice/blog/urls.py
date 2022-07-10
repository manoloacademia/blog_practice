""" This file shows the urls for blog app.
"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
]
