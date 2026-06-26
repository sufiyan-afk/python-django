from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login ,logout
from django.contrib.auth.models import User 
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# Create your views here.

def register_view(request):
    if request.method == 'POST':
        username = request.POST('username')
        password = request.POST('password')
        email = request.POST('email')
        
        
        # check if it is already exist or not?
        if User.objects.filter(username=username).exists():
            messages.error(request,"Username already taken!")
            return redirect('register')
        
        # Built-in helper -- password automatically hash hota hai
        user = User.objects.create_user(username = username , password = password , email = email)
        messages.error(request,"Account created ! please login.")
        return redirect('login')
    return render(request,"register.html")



#Login view

def login_view(request):
    if request.method == 'POST':
        username = request.POST('username')
        password = request.POST('password')
        
        
        #authenticate() --> DB me check karta , valid hai to User object return karta hai
        user = authenticate(request, username = username , password = password)
        
        if user is not None:
            login(request, user)     #session create hoti hai
            return redirect('dashboard')
        else:
            messages.error(request,"Invalid credentials!")
            return redirect('login')
        
    return render(request,"accoutns/login.html")



#Logout view
def logout_view(request):
    logout(request)          #session destroy karta hai
    return redirect('login')


#Protected Page -- @login_required decorator
@login_required(login_url='login')   # agar logged in nahi to login page pe bhejo
def dashboard_view(request):
    return render(request, "accounts/dashboard.html")
            