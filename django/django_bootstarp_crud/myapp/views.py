from django.shortcuts import render,redirect
from myapp.models import *

# Create your views here.

def index(request):
    products = product.objects.all()
    if request.method=='POST':
        name = request.POST['name']
        price = request.POST['price']
        qty = request.POST['qty']
        product.objects.create(name=name,price=price,qty=qty)
        return render(request,"index.html",{"products":products})
    else:
       return render(request,"index.html",{"products":products})
   
def delete_product(request):
    id = request.GET['id']
    prod = product.objects.get(pk=id)
    prod.delete()
    return redirect("index")

def edit_product(request):
    products = product.objects.all()
    if request.method=='POST':
        id = request.POST['id']
        name = request.POST['name']
        price = request.POST['price']
        qty = request.POST['qty']
        
        prod=product.objects.get(pk=id)
        prod.name = name
        prod.price = price
        prod.qty = qty
        prod.save()
        return render(request,"index.html",{"products":products})
    else:
        id = request.GET['id']
        prod = product.objects.get(pk=id)
        return render(request,"index.html",{"prod":prod,"products":products})