from django.shortcuts import render,redirect
from libraryapp.models import *
# Create your views here.

def index(request):
    if request.method == 'POST':
        data = request.POST
        title = data.get('title')
        author = data.get('author')
        genre = data.get('genre')
        price = data.get('price')
        Book.objects.create(title = title , author = author , genre =genre , price = price)
        return render(request,'index.html',{'msg':'book registred successfully!!!'})
    return render(request,'index.html') 

def display(request):
    books = Book.objects.all()
    return render(request,'display.html',{'books':books})

def update(request):
    id = request.GET.get('id')
    books = Book.objects.get(id = id)

    if request.method == 'POST':
        books.title = request.POST.get('title')
        books.author = request.POST.get('author')
        books.genre = request.POST.get('genre')
        books.price = request.POST.get('price')

        books.save()
        return redirect('display')
    return render(request,'update.html',{'books':books})

def delete(request):
    id = request.GET.get('id')
    Book.objects.get(id = id).delete()
    return redirect('display')