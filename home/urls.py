from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('prox5/', views.prox5, name='prox5'),
    path('photogrammetry/', views.photogrammetry, name='photogrammetry'),
    path('telecomsdatabase/', views.telecomsdatabase, name='telecomsdatabase'),
    path('search/', views.search, name='search'),
]
