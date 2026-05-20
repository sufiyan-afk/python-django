from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,"index.html")

def scorecard(request):
    return render(request,"scorecard.html")

def stats(request):
    return render(request,"stats.html")
