from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from papp.models import *

# Create your views here.

def index(request):
    if request.GET:
        cid = request.GET['cid']
        products = Product.objects.filter(category_id = cid)
    else:
        products = Product.objects.all()
    categories = Category.objects.all()
    return render(request,"index.html",{"products":products,"categories":categories})

@login_required(login_url="login-register")
def accounts(request):
    return render(request,"accounts.html")

@login_required(login_url="login-register")
def cart(request):
    return render(request,"cart.html")

@login_required(login_url="login-register")
def checkout(request):
    return render(request,"checkout.html")

def compare(request):
    return render(request,"compare.html")

def details(request):
    pid = request.GET['pid']
    product = Product.objects.get(pk=pid)
    return render(request,"details.html",{"product":product})

def login_register(request):
    return render(request,"login-register.html")

def shop(request):
    return render(request,"shop.html")

@login_required(login_url="login-register")
def wishlist(request):
    return render(request,"wishlist.html")

def user_registration(request):
    if request.method=='POST':
        data = request.POST
        uname = data.get('uname')
        email = data.get('email')
        password = data.get('pass')
        
        u = User(username=uname,email=email)
        u.set_password(password)
        u.save()
        return render(request,"login-register.html",{"msg":"registration successfully."})
    
def user_login(request):
    if request.method=='POST':
        data = request.POST
        uname = data.get('uname')
        password = data.get('pass')
        
        u = authenticate (username=uname,password=password)
        if u is not None:
            login(request,u)
            return redirect("index")
        else:
            return render(request,"login-register.html",{"err":"Invalid credentials."})
        
def user_logout(request):
    logout(request)
    return redirect("index")