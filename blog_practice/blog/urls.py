""" This file shows the urls for blog app.
"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.login_page, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('about/', views.about, name='about'),
    path('pages/', views.pages, name='pages'),
    path('pages/<int:pk>', views.page_detail, name='page_detail'),
    path('pages/create', views.page_create, name='page_create'),
    path('pages/<int:pk>/update', views.page_update, name='page_update'),
    path('pages/<int:pk>/delete', views.page_delete, name='page_delete'),
]
