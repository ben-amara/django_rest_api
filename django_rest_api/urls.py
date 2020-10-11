"""django_rest_api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
"""
# Django imports
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
urlpatterns = [
    # Examples:
    path('api/v1/', include('django_rest_api.rest_api.urls')),
]
