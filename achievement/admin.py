from django.contrib import admin

from achievement.models.achievement import Achievement, AchievementAdmin
from achievement.models.achievement_granted import AchievementGranted, AchievementGrantedAdmin
from achievement.models.achievement_level import AchievementLevel, AchievementLevelAdmin

admin.site.register(Achievement, AchievementAdmin)
admin.site.register(AchievementGranted, AchievementGrantedAdmin)
admin.site.register(AchievementLevel, AchievementLevelAdmin)
