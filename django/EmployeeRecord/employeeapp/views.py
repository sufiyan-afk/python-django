from django.shortcuts import render,redirect
from employeeapp.models import *
# Create your views here.

def index(request):
    if request.method == 'POST':
        data = request.POST
        name = data.get("name")
        email = data.get("email")
        department = data.get("department")
        salary = data.get("salary")
        Employee.objects.create(name = name , email = email , department = department ,salary = salary)
        return redirect("display")
    return render(request,"index.html")

def display(request):
    employees = Employee.objects.all()
    return render(request , 'display.html' ,{'employees':employees})

def update(request):
    id = request.GET.get('id')
    employee = Employee.objects.get(id =id)

    if request.method == 'POST':
        employee.name = request.POST.get('name')
        employee.email = request.POST.get('email')
        employee.department = request.POST.get('department')
        employee.salary = request.POST.get('salary')

        employee.save()
        return redirect('display')
    return render(request, "update.html",{"employee":employee})

def delete(request):
    id = request.GET.get('id')
    Employee.objects.get(id = id).delete()
    return redirect('display')