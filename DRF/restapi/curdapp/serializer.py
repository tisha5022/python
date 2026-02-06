# crudapp/serializer.py
from rest_framework import serializers
from curdapp.models import *

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"
        # fields = ["name","email"]
        # exclude = ['age']