from django.contrib import admin
from .models import PetProduct


class PetProductAdmin(admin.ModelAdmin):
    list_display= ('name', 'price','qty','img','desc','discount','date')

admin.site.register(PetProduct, PetProductAdmin)





