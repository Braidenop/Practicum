from django.urls import path
from . import views
from django.views.generic import TemplateView
from hospU.views import *

app_name = 'hospU'

urlpatterns = [
    path('', views.home, name='home'),
    path('login', views.LoginView.as_view(), name='login'),
    path('logout', views.LogoutView.as_view(), name='logout'),
    path('register', views.register, name='register'),

]