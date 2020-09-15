from django.urls import path

from boulder_stats.views.home import home


urlpatterns = [
    path('', home, name='home'),
]