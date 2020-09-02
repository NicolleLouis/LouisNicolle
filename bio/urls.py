from django.urls import path

from bio.views.home import home
from bio.views.medium import medium


urlpatterns = [
    path('', home, name='home'),
    path('medium', medium, name='medium'),
]
