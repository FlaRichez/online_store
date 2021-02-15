from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .filters import ProductFilter
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode

from .tokens import account_activation_token
from store.settings import EMAIL_HOST_USER
from .models import *
import products
from .forms import *
# Create your views here.

def products_page(request):
    products = Products.objects.all() #SELECT = FROM PRODUCTS
    filter = ProductFilter(request.GET,queryset=products)
    products = filter.qs
    return render(request,'products/products.html',{"products":products,'filter':filter})


def order_page(request,products_id):
    try:
        profile = Profile.objects.get(user=request.user)
        product = Products.objects.get(id=products_id)
        form = OrderForm(initial={'product':product,'user':request.user,})
        total_price = 0
        if request.method == 'POST':
            form = OrderForm(request.POST)
            if form.is_valid():
                if 20<profile.order_count<40:
                    profile.sale_amount = 0.1
                    total_price = (product.price - product.price * profile.sale_amount) * form.cleaned_data['quantity']
                elif 40<profile.order_count<60:
                    profile.sale_amount = 0.2
                    total_price = (product.price - product.price * profile.sale_amount) * form.cleaned_data['quantity']
                if product.sale:
                    total_price = total_price - total_price * 0.2
                if form.cleaned_data['payment_method'] == "wallet":
                    if profile.wallet >= total_price:
                        profile.wallet -= total_price
                        profile.order_count += 1
                        profile.save()
                        return HttpResponse('Thanks for buying!')
                    else:
                        return HttpResponse('Not enough money')
                form.save()
                profile.order_count += 1
                profile.save()

        return render(request,'products/order.html',{"form":form,"total_price":total_price,})
    except Products.DoesNotExist:
        return HttpResponse('Not Found:')




def register_page(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            mail_subject = 'Activate your blog account.'
            message = render_to_string('products/acc_active_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            to_email = form.cleaned_data.get('email')
            email = EmailMessage(
                mail_subject, message, to=[to_email]
            )
            email.send()
            return HttpResponse('Please confirm your email address to complete the registration')
    else:
        form = SignupForm()
    return render(request,'products/register.html', {'form': form})

def activate_page(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        # return redirect('home')
        return HttpResponse('Thank you for your email confirmation. Now you can login your account.')
    else:
        return HttpResponse('Activation link is invalid!')


def user_list(request,user_id):
    user = User.objects.get(id=user_id)
    orders = user.order_set.all()
    context = {'user':user,'orders':orders}
    return render(request,'products/userlist.html',context)



def contacts_page(request):
    contacts = Contacts.objects.all()
    contact = {'contacts':contacts}
    return render(request,'products/contacts.html',contact)



def update_order(request,order_id):
    order = Order.objects.get(id=order_id)
    form = OrderForm(instance=order)
    if request.method == 'POST':
        form = OrderForm(request.POST,instance=order)
        form.save()
        return redirect('products')
    return render(request,'products/order.html',{'form':form})



def delete_order(request,order_id):
    order = Order.objects.get(id=order_id)
    order.delete()
    return redirect('products')


def aboutus_page(request):
    about_us = AboutUs.objects.all()
    context = {'about_us':about_us}
    return render(request,'products/aboutus.html',context)


def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username=username,password=password)
        login(request,user)
        return redirect('products')

    return render(request,'products/login.html')


def logout_page(request):
    logout(request)
    return redirect('/')


def account_settings(request):
    user = request.user.profile
    form = ProfileForm(instance=user)
    order_user = request.user
    orders = order_user.order_set.all()
    if request.method == 'POST':
        form = ProfileForm(request.POST,request.FILES,instance=user)
        if form.is_valid():
            form.save()
    context = {'form':form,'orders':orders}
    return render(request,'products/profile.html',context)
