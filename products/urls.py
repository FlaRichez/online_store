from django.contrib.auth.views import PasswordResetView
from django.urls import path
from .views import products_page, order_page, user_list, contacts_page, update_order, delete_order, \
    aboutus_page, login_page, logout_page, account_settings, activate_page, register_page,activate_page
from django.contrib.auth import views as a_views




urlpatterns = [
    path("",products_page,name='products'),
    path('order/<int:products_id>/',order_page,name='order'),
    path('update_order/<int:order_id>/',update_order,name='update_order'),
    path('delete_order/<int:order_id>/',delete_order,name='delete_order'),
    path('register/',register_page,name='register'),
    path('activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',activate_page, name='activate'),
    path('users/<int:user_id>/',user_list,name='user-list'),
    path('contacts/',contacts_page,name='contacts-page'),
    path('aboutus/',aboutus_page,name='aboutus'),
    path('login/',login_page,name='login-page'),
    path('logout/',logout_page,name='logout'),
    path('profile/',account_settings,name='profile'),
    path('reset_password/',a_views.PasswordResetView.as_view(template_name='user_dir'),name='password_reset'),
    path('reset_password_done/',a_views.PasswordResetDoneView.as_view(),name='password_reset_done'),
    path('reset/<uidb64>/<token>',a_views.PasswordResetConfirmView.as_view(),name='password_reset_confirm'),
    path('reset_password_complete/',a_views.PasswordResetCompleteView.as_view(),name='password_reset_complete'),
]