from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
    path("404/", views.error404, name="404"),
    # Authentication
    path("profile/", views.profile, name="profile"),
    path("login/", views.login, name="login"),
    path("register/", views.register, name="register"),
]
