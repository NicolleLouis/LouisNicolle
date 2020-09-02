from django.urls import path

from bio.views.home import home


urlpatterns = [
    path('', home, name='home'),
]
