from django.shortcuts import render
from myapp.models import *
from django.http import JsonResponse,HttpResponse
from django.db.models import Q

# Create your views here.

def index(request):
    return render(request,'index.html')

def register(request):
    if request.method == 'POST':
        data = request.POST
        name = data.get('name')
        email = data.get('email')
        phone = data.get('phone')
        
        Student.objects.create(name= name,email=email,phone=phone)
        
        return HttpResponse("registartion successfully !")
    
def display(request):
    students = Student.objects.all()
    return JsonResponse({"students":list(students.values())})

def delete_student(request):
    sid = request.GET['sid']
    st = Student.objects.get(pk=sid)
    st.delete()
    return HttpResponse("Student Deleted")

def getbyid(request):
    sid = request.GET['sid']
    st = Student.objects.filter(id=sid)
    return JsonResponse({"student":list(st.values())})

def update_student(request):
    
    if request.method=='POST':
        data = request.POST
        id = data.get('id')
        name = data.get('name')
        email = data.get('email')
        phone = data.get('phone')

        st = Student.objects.get(pk=id)
        st.name = name
        st.email = email
        st.phone = phone
        st.save()   
    

        return HttpResponse("Update successfully")
    
def search(request):
    value = request.GET['value']
    students = Student.objects.filter(name__startswith=value) |Student.objects.filter(email__startswith=value) | Student.objects.filter(phone__startswith=value)

    # students = Student.objects.filter(Q(name__startswith=value)|Q(email__startswith=value)|Q(phone__startswith=value)) 


    return JsonResponse({"students":list(students.values())})