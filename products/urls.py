from django.urls import path
from .views import products_page, order_page, creation_page, user_list





urlpatterns = [
    path("",products_page,name='products'),
    path('order/',order_page),
    path('creation/',creation_page),
    path('users',user_list),
]