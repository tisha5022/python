from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from papp.models import *
from django.http import JsonResponse,HttpResponse
import razorpay
import datetime
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.

def index(request):
    # if request.GET:
    #     cid = request.GET['cid']
    #     products = Product.objects.filter(category_id = cid)
    # else:
    #     products = Product.objects.all()
    # categories = Category.objects.all()
    # return render(request,"index.html",{"products":products,"categories":categories})
    return render(request,"index.html")

def get_products(request):
    catid = request.GET['catid']
    if int(catid) >0:
        products = Product.objects.filter(category_id=catid)
        return JsonResponse({"products":list(products.values())})
    else:
        products = Product.objects.all()
        return JsonResponse({"products":list(products.values())}) 
    
def search_products(request):
        q = request.GET['q']
        products = Product.objects.filter(name__startswith=q)
        return JsonResponse({"products":list(products.values())})

def get_categories(request):
    categories = Category.objects.all()
    return JsonResponse({"categories":list(categories.values())})

@login_required(login_url="login-register")
def accounts(request):
    orders = Order.objects.filter(user=request.user)
    return render(request,"accounts.html",{"orders":orders})

@login_required(login_url="login-register")
def cart(request):
    carts = Cart.objects.filter(user=request.user)

    sum = 0
    
    for c in carts:
        sum+=c.total_price()

    return render(request, 'cart.html',{"carts":carts,"total":int(sum)})

def addtocart(request):
    pid = request.GET['pid']
    product = Product.objects.get(pk=pid)
    user = request.user
        
    if user.is_anonymous:
        return HttpResponse(user)
    else:
        isexist = Cart.objects.filter(user=user,product=product)
        if (len(isexist)>=1):
            isexist[0].qty = isexist[0].qty+1
            isexist[0].save()
            return HttpResponse("Product added into cart")
        else:
            Cart.objects.create(product=product,user=user,qty=1)
            return HttpResponse("Product added into cart")

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

def removecart(request):
    cid = request.GET['cid']
    cart = Cart.objects.get(pk=cid)
    cart.delete()
    return HttpResponse("Cart deleted")

def changeqty(request):
    cid = request.GET['cid']
    qty = request.GET['qty']
    cart = Cart.objects.get(pk=cid)

    if int(qty)<=0:
        cart.delete()
    else:
        cart.qty = qty
        cart.save()
    return HttpResponse("Cart updated")

def payment(request):

    amt = request.GET['amt']
    client = razorpay.Client(auth=("rzp_test_S1Hsg7YN8MlwDU", "ZKs1rK1XnjRDNd4uxjP2NcRJ"))

    
    data = { "amount": int(amt)*100, "currency": "INR", "receipt": "order_rcptid_11" }
    payment = client.order.create(data=data) # Amount is in currency subunits.
    
    return JsonResponse(payment)


def makeorder(request):
    payid = request.GET['payid']
    date = datetime.datetime.now()
    user = request.user

    carts = Cart.objects.filter(user=user)
    sum = 0
    for i in carts:
        sum += i.total_price()

    order = Order.objects.create(user=user,date=date,total=sum,payid=payid)

    rows = ""
    count = 0
    for c in carts:
        OrderDetails.objects.create(order=order,product=c.product,qty=c.qty,price=c.product.price)
        rows+=f"<tr><td>{count}</td><td>{c.product.name}</td><td>{c.product.price}</td><td>{c.qty}</td><td>{c.total_price()}</td></tr>"
        c.delete()
        count+=1
        
    tbl = f"<table border='2'><thead><tr><th>PayID : {order.payid}</th><th>PayType : {order.paytype}</th><th>Total</th></tr><tr><th>Order Date : {order.date}</th><th>Status : {order.status}</th><th>{order.total}</th></tr><tr><th>Id</th><th>Name</th><th>Price</th><th>Qty</th><th>total</th></tr></thead><tbody>{rows}</tbody></table>"
                    
                   
                    
                  
        
    try:
            send_mail("Order Confimation", "Your order placed successfully", 
            settings.EMAIL_HOST_USER, [user.email],html_message=tbl)
            
    except Exception as e:
            print(e)
     
    return HttpResponse("order placed successfully")