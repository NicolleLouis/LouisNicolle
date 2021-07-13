from django.urls import path

from stats.views.profile import ProfileView

urlpatterns = [
    path('profile', ProfileView.as_view()),
]
