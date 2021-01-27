from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

import products
from .forms import *
# Create your views here.

def products_page(request):
    products = Products.objects.all() #SELECT = FROM PRODUCTS
    return render(request,'products/products.html',{"products":products})

def order_page(request):
    form = OrderForm()
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
    return render(request,'products/order.html',{"form":form})


def creation_page(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('products')
    return render(request,'products/creation.html',{"form":form})


def user_list(request):
    users = User.objects.all()
    context = {'users':users}
    return render(request,'products/userlist.html',context)