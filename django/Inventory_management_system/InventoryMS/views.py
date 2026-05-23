from django.shortcuts import render,redirect
from InventoryMS.models import *
# Create your views here.

def index(request):
    if request.method == 'POST':
        data = request.POST
        name = data.get('name')
        category = data.get('category')
        price = data.get('price')
        quantity = data.get('quantity')
        Product.objects.create(name = name , category = category , price = price , quantity = quantity)
        return render(request,'index.html',{'msg':'added successfully!!'})
    return render(request,'index.html')

def display(request):
    products = Product.objects.all()
    return render(request,'display.html',{'products':products})



def update(request):
    id = request.GET.get('id')
    products = Product.objects.get(id = id)

    if request.method == 'POST':
        products.name = request.POST.get('name')
        products.category = request.POST.get('category')
        products.price = request.POST.get('price')
        products.quantity = request.POST.get('quantity')
        products.save()

        return redirect('display')
    return render(request,'update.html',{'products':products})



def delete(request):
    id = request.GET.get('id')
    Product.objects.get(id = id).delete()
    return redirect('display')