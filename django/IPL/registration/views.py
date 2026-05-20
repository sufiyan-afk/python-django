from django.shortcuts import render
from registration.models import*
# Create your views here.

def index(request):
    return render(request,"index.html")

def reg(request):
    if request.method == "POST":
        data = request.POST
        name = data.get("name")
        age = data.get("age")
        role = data.get("role")
        state = data.get("state")
        Players.objects.create(name = name , age = age , role = role ,state = state)
        return render(request,"index.html",{"success":"player registered successfully"})