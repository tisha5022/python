from django.urls import path
from company.views import *

urlpatterns = [
    path("depts",Deptapi.as_view()),
    path("depts/<id>",DeptUpdateAPI.as_view()),
    path("emps/dept/<id>",addEmp,name="addemp"),
    path("emps",getemps,name="emps"),
    path("emps/dept/<id>/<eid>",updateEmp,name="updateemp"),
    path("emps/<id>",EmpById.as_view())
]
