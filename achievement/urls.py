from django.urls import path

from achievement.views.generate_achievement import GenerateAchievementView
from achievement.views.profile_achievement import ProfileAchievementView

urlpatterns = [
    path('generate', GenerateAchievementView.as_view()),
    path('profile/<int:profile_id>', ProfileAchievementView.as_view()),
]
