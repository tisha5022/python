from django.shortcuts import render,redirect
from myapp.models import *

# Create your views here.

def index(request):
    products = product.objects.all()
    categories = Category.objects.all()
    if request.method=='POST':
        cat = request.POST['cat']
        name = request.POST['name']
        price = request.POST['price']
        qty = request.POST['qty']
        image = request.FILES['image']
        category = Category.objects.get(pk=cat)
        
        product.objects.create(name=name,price=price,qty=qty,image=image,category=category)
        return render(request,"index.html",{"products":products,"categories":categories})
    else:
       return render(request,"index.html",{"products":products,"categories":categories})
   
def delete_product(request):
    id = request.GET['id']
    prod = product.objects.get(pk=id)
    prod.delete()
    return redirect("index")

def edit_product(request):
    products = product.objects.all()
    categories = Category.objects.all()
    if request.method=='POST':
        cat = request.POST['cat']
        id = request.POST['id']
        name = request.POST['name']
        price = request.POST['price']
        qty = request.POST['qty']
        
        prod=product.objects.get(pk=id)
        prod.name = name
        prod.price = price
        prod.qty = qty
        prod.category = Category.objects.get(pk=cat)

        if request.FILES:
            prod.image = request.FILES['image']
        
        prod.save()
        return render(request,"index.html",{"products":products,"categories":categories})
    else:
        id = request.GET['id']
        prod = product.objects.get(pk=id)
        return render(request,"index.html",{"prod":prod,"products":products,"categories":categories})