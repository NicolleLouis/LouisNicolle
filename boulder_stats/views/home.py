from django.shortcuts import render


def home(request):
    context = {
        "title": "Home"
    }
    return render(request, "boulder_stats/home.html", context)
