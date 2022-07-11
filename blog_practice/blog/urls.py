""" This file shows the urls for blog app.
"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('pages/', views.pages, name='pages'),
    path('pages/<int:pk>', views.page_detail, name='page_detail'),
]
