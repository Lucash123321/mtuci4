from django.contrib import admin
from django.urls import path, include
from fingerprints import views


app_name = "fingerprints"

urlpatterns = [
    path('create/', views.create_fingerprint, name='create_fingerprint'),
]
