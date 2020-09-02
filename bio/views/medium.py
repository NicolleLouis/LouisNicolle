from django.shortcuts import render


def medium(request):
    context = {
        "title": "Medium"
    }
    return render(request, "bio/medium.html", context)
