from django.shortcuts import render, redirect
from django.http import HttpResponse


def home_view(request):
    return render(request, "home.html", {})


def about(request):
    return render(request, "pages/about.html")


def contact(request):
    return render(request, "pages/contact.html")
