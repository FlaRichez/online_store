from django.contrib.auth.models import User
from django.db import models
from datetime import date
# Create your models here.
class Products(models.Model):
    types = (
        ('Toyota','Toyota'),
    )

    name = models.CharField(max_length=50)
    description = models.TextField()
    type = models.CharField(max_length=50,choices=types)
    price = models.IntegerField()
    image = models.ImageField(blank=True,null=True,default='default_product_image.png')
    sale = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name}" f"{self.price}"
class Order(models.Model):
    statuses = (
        ('In process', 'In process'),
        ('Delivered', 'Delivered'),
        ('Not Delivered', 'Not Delivered'),
    )
    p_method = (
        ('money', 'money'),
        ('wallet', 'wallet'),
    )
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    product = models.ForeignKey(Products,on_delete=models.SET_NULL,null=True)
    quantity = models.IntegerField(default=1)
    status = models.CharField(max_length=20,choices=statuses,default=1)
    date_created = models.DateTimeField(auto_now_add=True)
    payment_method = models.CharField(max_length=20,choices=p_method)





class AboutUs(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()


class Contacts(models.Model):
    phone = models.CharField(max_length=10)
    email = models.CharField(max_length=50)
    address = models.TextField(max_length=500)
    face = models.TextField(max_length=200)


class Profile(models.Model):
    genders = (
        ('F','F'),
        ('M','M'),
    )
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    image = models.ImageField(default='index.jpeg',blank = True)
    full_name = models.CharField(max_length=50)
    gender = models.CharField(choices=genders, max_length=20)
    description = models.TextField()
    birth_date = models.DateField(default=date.today())
    twitter_link = models.CharField(max_length=50)
    wallet = models.PositiveIntegerField(default=0)
    order_count = models.PositiveIntegerField(default=0)
    sale_amount = models.FloatField(default=0.001)
