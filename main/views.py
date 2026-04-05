from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from .forms import RegistrationForm


def index(request):
    return render(request, 'main/index.html')

def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('orders')
        else:
            context = {'error': 'Невірний email або пароль'}
            return render(request, 'registration/login.html', context)
    return render(request, 'registration/login.html')


def register_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            
            # Create user with email as username
            user = User.objects.create_user(
                username=email,
                email=email,
                password=password,
                first_name=first_name,
                last_name=last_name
            )
            
            # Authenticate and login
            user = authenticate(request, username=email, password=password)
            login(request, user)
            return redirect('orders')
        else:
            context = {'form': form, 'errors': form.errors}
            return render(request, 'registration/register.html', context)
    else:
        form = RegistrationForm()
        context = {'form': form}
        return render(request, 'registration/register.html', context)


def logout_view(request):
    logout(request)
    return redirect('index')