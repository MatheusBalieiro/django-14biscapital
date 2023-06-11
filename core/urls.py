from django.contrib import admin
from django.urls import path, re_path
from django.views.static import serve
from django.conf import settings
from app.home import home_views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("home/", home_views),
    re_path(r"^static/(?P<path>.*)$", serve, {"document_root": settings.MEDIA_ROOT}),
]
