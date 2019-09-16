from django.contrib import admin
from django.urls import path

from register import views

urlpatterns = [
    path('register', views.register),

    path('register_ok/<name>', views.register_ok),
    path('', views.register_page),
]
