
from django.contrib import admin
from django.urls import path,include
from .import views
urlpatterns = [
    path("",views.Indexinfo,name="Indexinfo"),
    path("addmovieinfo",views.addmovieinfo,name="addmovieinfo"),
    path("movieinfo",views.movieinfo,name="movieinfo"),
]
