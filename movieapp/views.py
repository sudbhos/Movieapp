from django.shortcuts import render
from .import forms
from.models import Movie
# Create your views here.

def Indexinfo(request):
    return render(request,"testapp/index.html")

def addmovieinfo(request):
    form=forms.Moviedetails()
    if request.method=="POST":
        form=forms.Moviedetails(request.POST)
        if form.is_valid():
            form.save(commit=True)
            print("Form uploaded successfully.")
        return Indexinfo(request)
    return render(request,"testapp/addmovie.html",{"form":form})

def movieinfo(request):
    my_movie=Movie.objects.all()
    return render(request,"testapp/movielist.html",{"my_movie":my_movie})

