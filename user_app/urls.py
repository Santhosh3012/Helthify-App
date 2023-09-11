from django.urls import path
from . import views
from . views import *
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),

    path('register/', register, name='register'),
    path('send_email_two/',send_email_two, name='send_email_two'),
    # path('regsuccess/',regsuccess, name='regsuccess'),
    path('login/', login, name='login'),
    path('login_success/',login_success,name='login_success'),
    path('profile_view/<int:user_id>/',profile_view,name='profile_view'),
    # path('profile_view/', profile_view, name='profile_view'),

    # path('reset-password/<str:reset_token>/',reset_password, name='reset_password'),
    path('change_password/',change_password, name='change_password'),
    path('email_template/',email_template,name='email_template'),
    path('password_reset/sent/',password_reset_sent, name='password_reset_sent'),
    path('password_change_success/',password_change_success, name='password_change_success'),
    # path('verify_otp/',verify_otp, name='verify_otp'),
    # path('display_otp/',display_otp, name='display_otp'),
    path('forget_password/', forget_password, name='forget_password'),
    path('dashboard/', dashboard, name='dashboard'),
    path('delete/<int:user_id>/', delete_user, name='delete_user'),

    # path('logout/', logout, name='logout'),
    path('logout/', custom_logout, name='custom_logout'),


]
