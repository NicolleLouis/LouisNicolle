from django.urls import path

from climax_tracker.views.profile import ProfileView

urlpatterns = [
    path('profile', ProfileView.as_view()),
]
