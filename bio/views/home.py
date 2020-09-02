from django.shortcuts import render


def home(request):
    context = {
        "title": "Louis Nicolle Bio"
    }
    return render(request, "bio/home.html", context)
