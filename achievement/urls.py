from django.urls import path

from achievement.views.generate_achievement import GenerateAchievementView

urlpatterns = [
    path('generate/achievement', GenerateAchievementView.as_view()),
]
