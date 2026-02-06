from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from curdapp.models import *
from curdapp.serializer import *

@api_view(['GET'])
def view_student(request):
    students = Student.objects.all()
    ser = StudentSerializer(students, many=True)
    return Response({"data":ser.data})

@api_view(['POST'])
def add_student(request):
    stdata = request.data
    ser = StudentSerializer(data = stdata)
    if not ser.is_valid():
        return Response({"errors":ser.errors,"message":"Something went wrong"})
    else:
        ser.save()
        return Response({"data":ser.data,"message":"Data inserted successfully"})
    
@api_view(['GET'])
def view_byid(request,id):
    student = Student.objects.get(pk=id)
    ser = StudentSerializer(student)
    return Response({"data":ser.data})

@api_view(['PUT'])
def update_student(request,id):
    sdata = request.data
    cdata = Student.objects.get(pk=id)
    ser = StudentSerializer(cdata,sdata,partial=True)
    if not ser.is_valid():
        return Response({"errors":ser.errors,"message":"Something went wrong"})
    else:
        ser.save()
        return Response({"data":ser.data,"message":"Data update successfully"})
    
@api_view(['DELETE'])
def delete_student(request,id):
    sdata = Student.objects.get(pk=id)
    sdata.delete()
    return Response({"message":"Data deleted"})