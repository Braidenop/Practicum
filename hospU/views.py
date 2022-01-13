from django.shortcuts import render, redirect
from django.views.generic import ListView

from django.contrib.auth import authenticate, login, logout
from django.views.generic import FormView
from django.urls import reverse, reverse_lazy
from django.contrib.auth import views as auth_views

from .forms import RegistrationForm

def home(request):
    return render(request, 'homeU/base.html')

def register(request):
    title = "Crea una cuenta"
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/login')
    else:
        form = RegistrationForm()

    context = {'form': form, 'title': title}
    return render(request, 'homeU/register.html', context=context)


class LoginView(auth_views.LoginView):
    """Login view."""
    template_name = 'homeU/login.html'


