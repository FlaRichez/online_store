from django.contrib import admin
from .models import *
# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'image', 'description', 'price',)
admin.site.register(Products,ProductAdmin)

admin.site.register([Order,AboutUs,Contacts,Profile])
























