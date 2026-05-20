from django.shortcuts import render
from movie_review.models import *
# Create your views here.

def index(request):
    return render(request,"index.html")

def reg(request):
    if request.method == "POST":
        data = request.POST
        movie_name = data.get("movie_name")
        hero_name = data.get("movie_name")
        rating = data.get("movie_name")
        Netflix.objects.create(movie_name = movie_name , hero_name = hero_name , rating = rating)
        return render(request,"index.html",{"msg":"Review Submitted Successfully !"})
