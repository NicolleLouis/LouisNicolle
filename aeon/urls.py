from django.urls import path, include

from aeon.views.home import home

urlpatterns = [
    path('', home),
]
