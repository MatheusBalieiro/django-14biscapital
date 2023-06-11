from django.shortcuts import render, redirect
from django.http import HttpResponse


def index(request):
    return render(request, "index.html")


def about(request):
    return render(request, "pages/about.html")


def contact(request):
    return render(request, "pages/contact.html")


def error404(request):
    return render(request, "pages/404.html")


def profile(request):
    return render(request, "accounts/profile.html")


def login(request):
    return render(request, "accounts/login.html")


def register(request):
    return render(request, "accounts/register.html")
