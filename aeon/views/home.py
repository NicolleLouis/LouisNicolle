from django.shortcuts import render


def home(request):
    return render(request, 'aeon/home_aeon.html')
