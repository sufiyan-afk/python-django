from django.shortcuts import render,redirect
from studentapp.models import *
# Create your views here.

def index(request):
    if request.method == 'POST':
        data = request.POST
        name = data.get("name")
        email = data.get("email")
        age = data.get("age")
        Student.objects.create(name = name , email = email , age = age)
        return render(request,"index.html" , {'msg':'Student added successfully'})
    students = Student.objects.all()
    return render(request , "index.html" , {"students":students})

def display(request):
    students = Student.objects.all()
    return render(request,"display.html",{'students':students})

def update(request):
    id = request.GET.get('id')
    student = Student.objects.get(id = id)
    if request.method == "POST":
        student.name = request.POST.get("name")
        student.email = request.POST.get("email")
        student.age = request.POST.get("age")
        student.save()
        return redirect("display")
    
    return render(request , "update.html" ,{"student" : student})

def delete(request):
    id= request.GET.get('id')
    Student.objects.get(id=id).delete()
    return redirect("display")
