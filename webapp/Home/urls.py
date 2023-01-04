from django.contrib import admin
from django.urls import path
from Home import views

urlpatterns = [
    path("",views.index,name='blank'),
    path("HOME",views.index,name='Home'),
    path("ABOUT",views.about,name='ABOUT'),
    path("REGISTRATION",views.registration,name='REGISTRATION'),
    path("COMMITTEES",views.committees,name='COMMITTEES'),
]
