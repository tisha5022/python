from django.contrib import admin
from myapp.models import *

# Register your models here.

class studentAdmin(admin.ModelAdmin):
    list_display = ('name','email','age')

admin.site.register(student,studentAdmin)