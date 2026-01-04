from django.contrib import admin
from myapp.models import *

# Register your models here.

class ContryAdmin (admin.ModelAdmin):
    list_display = ['name']
class StateAdmin (admin.ModelAdmin):
    list_display = ['name']
class CityAdmin (admin.ModelAdmin):
    list_display = ['name']

admin.site.register(Product)
admin.site.register(Country,ContryAdmin)
admin.site.register(State,StateAdmin)
admin.site.register(City,CityAdmin)