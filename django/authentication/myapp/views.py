from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']
        u = authenticate(username=username,password=password)
        if u is None:
            return render(request,"index.html",{"err":"Invalid credentials"})
        else:
            login(request,u)
            return redirect("home")
        
    return render(request,"index.html")

def reg(request):
    if request.method=='POST':
        fname = request.POST['fname']
        lname = request.POST['lname']
        username = request.POST['username']
        password = request.POST['password']
        
        if User.objects.filter(username=username).exists():
            return render(request,"registration.html",{"err":"Username alredy exist !"})
        else:   
            u = User(first_name=fname,last_name=lname,username=username)
            u.set_password(password)
            u.save()
            return render(request,"registration.html",{"msg":"Registration Successfully Done !"})
    
    return render(request,"registration.html")

@login_required(login_url="index")
def home(request):
    return render(request,"home.html")

def user_logout(request):
    logout(request)
    return render(request,"index.html")