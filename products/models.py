from django.db import models

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


    def __str__(self):
        return f"{self.name}"
class Order(models.Model):
    statuses = (
        ('In process', 'In process'),
        ('Delivered', 'Delivered'),
        ('Not Delivered', 'Not Delivered'),
    )
    product = models.ForeignKey(Products,on_delete=models.SET_NULL,null=True)
    quantity = models.IntegerField(default=1)
    status = models.CharField(max_length=20,choices=statuses,default=1)
    date_created = models.DateTimeField(auto_now_add=True)


class AbouTus(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()





