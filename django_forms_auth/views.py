from django.shortcuts import render, redirect

from django_forms_auth.forms import RegisterForm, LoginForm
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.views import LoginView
# Create your views here.

import requests

# requests.post()


def index(request):
    return render(request, "index.html")


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            # Add Some other Logic here
            username = form.cleaned_data.get('username')

            messages.success(
                request, f"Account have been created successfully for {username}")

            return redirect("index")

        else:
            if form.errors:
                for field in form:
                    for error in field.errors:
                        messages.error(request, error)

                return redirect('register')

    context = {

        'form': RegisterForm()
    }
    return render(request, 'register.html', context)


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)

            print("Logged in ")
            messages.success(
                request, f"{user.username}, You have successfully logged in")

            return redirect('index')

        else:
            print("didn't work")
            messages.error(request, "invalid credentials")

            return redirect('login')

    context = {
        'form': LoginForm()
    }
    return render(request, 'login.html', context)


def logout_view(request):
    if request.user.is_authenticated:
        logout(request)
        messages.success(request, f'you have logged out succesfully')
        return redirect('login')


def changepassword(request):
    form = PasswordChangeForm(user=request.user)

    if request.method == 'POST':
        form = PasswordChangeForm(request.POST, user=request.user,)
        if form.is_valid():
            form.save()

            print("password changed successfully")

        else:
            if form.errors:
                for field in form:
                    for error in field.errors:
                        print(error)
                        messages.error(request, error)

    return render(request, 'changepassword.html', {'form': form})
