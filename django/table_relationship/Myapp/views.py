from django.shortcuts import render,redirect
from Myapp.models import *
# Create your views here.

def home(request):
    #------ One to One -------
    if request.method == 'POST' and 'save_passport' in request.POST:
        name = request.POST.get('name')
        country = request.POST.get('country')
        pid = request.POST.get('pid')
        person = Person.objects.create(name = name)
        Passport.objects.create(person = person , country = country , pid =pid)

    #-----One to many ----
    if request.method == 'POST' and 'save_product' in request.POST:
        category_id = request.POST.get('category')
        pname = request.POST.get('pname')
        price = request.POST.get('price')
        quantity = request.POST.get('quantity')
        
        category = Category.objects.get(id = category_id)
        Product.objects.create(category = category , name = pname , price = price , quantity = quantity)
        
    #----many to many ----
    if request.method == 'POST' and 'save_author' in request.POST:
        author_name = request.POST.get('author_name')
        book_ids = request.POST.get('books')        
        
        author = Author.objects.create(name = author_name)
        author.book.set(book_ids)
        
      # ---- READ — sabka data template ko do ----
    context = {
        'passports'  : Passport.objects.select_related('person').all(),
        'categories' : Category.objects.all(),
        'products'   : Product.objects.select_related('category').all(),
        'books'      : Book.objects.all(),
        'authors'    : Author.objects.prefetch_related('book').all(),
    }
    
    return render(request, 'index.html' , context)

# ======  Passport Update and delete ====

def edit_passport(request,id):
    passport = Passport.objects.get(id = id)
    
    if request.method == 'POST':
        passport.person.name = request.POST.get('name')
        passport.person.save()
        passport.country = request.POST.get('country')
        passport.pid = request.POST.get('pid')
        passport.save()
        return redirect('home')
    
    return render(request, 'edit_passport.html' , {'passport':passport})

def delete_passport(request,id):
    passport = Passport.objects.get(id = id)
    
    passport.person.delete() 
    return redirect('home')



#===== Product Update / Delete ====

def edit_product(request, id):
    product = Product.objects.get(id = id)
    categories = Category.objects.all()
    
    if request.method == 'POST':
        category_id = request.POST.get('category')
        product.category = Category.objects.get(id = category_id)
        product.name = request.POST.get('pname')
        product.price = request.POST.get('price')
        product.quantity = request.POST.get('quantity')
        product.save()
        return redirect('home')
    return render(request , 'edit_product.html' , {'product':product , 'categories':categories})

def delete_product(request , id):
    product = Product.objects.get(id = id)
    product.delete()
    return redirect('home')



#==== Author update / Delete ====

def edit_author(request , id):
    author = Author.objects.get(id = id)
    books = Book.objects.all()

    if request.method == 'POST':
        author_name = request.POST.get('author_name')
        book_ids = request.POST.get('books')
        author.save()
        author.book.set(book_ids)
        return redirect('home')
    return render(request , 'edit_author.html' ,{
        'author':author,
        'books':books,
    })
    
def delete_author(request , id):
    author = Author.objects.get(id = id)
    author.delete()
    return redirect('home')