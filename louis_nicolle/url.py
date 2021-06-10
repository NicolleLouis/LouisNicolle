from louis_nicolle.views.home import home
from django.urls import path

urlpatterns = [
    path('', home),
]
