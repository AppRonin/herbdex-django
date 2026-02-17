from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('about/', views.about, name='about'),
    path('', views.catalog, name='catalog'),
    path('<slug:herb_slug>/', views.herb_detail, name='herb_detail'),
]
