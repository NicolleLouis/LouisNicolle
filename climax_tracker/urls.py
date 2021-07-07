from django.urls import path

from climax_tracker.views.florent import FlorentView
from climax_tracker.views.profile import ProfileView
from climax_tracker.views.profile_detail import ProfileDetailView

urlpatterns = [
    path('profile', ProfileView.as_view()),
    path('profile/<int:profile_id>', ProfileDetailView.as_view()),
    path('florent', FlorentView.as_view()),
]
