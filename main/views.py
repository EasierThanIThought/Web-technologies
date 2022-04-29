from django.shortcuts import render, redirect
from .forms import *
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages


def index(request):
    return render(request, "main/index.html")


def about(request):
    return render(request, "main/about.html")


def message(request):
    error = ''
    if request.method == "POST":
        form = FeedBackForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Homepage')
        else:
            error = 'Форма заполнена неверно'
    form = FeedBackForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, "main/message.html", context)


def registration(request):
    return render(request, "main/registration.html")


def authorization(request):
    return render(request, "main/authorization.html")


def personpage(request):
    return render(request, "main/personpage.html")


def clinic(request):
    return render(request, "main/clinic.html")


def home(request):
    return render(request, "main/home.html")


def register(request):
    error = ''
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Clinic')
        else:
            error = 'Форма заполнена неверно'
    form = FeedBackForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, "main/register.html", context)


