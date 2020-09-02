from django.contrib import admin
from django.shortcuts import render
from django.urls import path, include


def home(request):
    context = {
        "title": "Home"
    }
    return render(request, "LouisNicolle/home.html", context)


urlpatterns = [
    path('', home),
    path('admin/', admin.site.urls),
    path('bio/', include("bio.urls")),
]
