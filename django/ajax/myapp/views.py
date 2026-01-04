from django.shortcuts import render
from django.http import HttpResponse
from myapp.models import *
from django.http import JsonResponse

# Create your views here.

def index(request):
    return render(request,"index.html")

def view(request):
    data = request.GET['data']
    products = Product.objects.filter(name__startswith=data)
    return JsonResponse({"products":list(products.values())})    
    # return  HttpResponse(f"hello {data}")
    
def countries(request):
    countries = Country.objects.all()
    return JsonResponse({"countries":list(countries.values())})  

def states(request):
    cid = request.GET['cid']
    states = State.objects.filter(country_id=cid) 
    return JsonResponse({"states":list(states.values())}) 

def cities(request):
    sid = request.GET['sid']
    cities = City.objects.filter(state_id=sid) 
    return JsonResponse({"cities":list(cities.values())}) 