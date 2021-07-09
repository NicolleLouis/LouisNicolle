from django.db import models
from django.contrib import admin

from stats.models.profile import Profile


class AchievementGranted(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(
        Profile,
        on_delete=models.PROTECT,
    )
    achievement = models.ForeignKey(
        'Achievement',
        on_delete=models.PROTECT,
    )
    achievement_level = models.ForeignKey(
        'AchievementLevel',
        null=True,
        blank=True,
        on_delete=models.PROTECT,
    )
    granted_at = models.DateTimeField(
        auto_now_add=True,
    )

    def __str__(self):
        return '{} - {}'.format(str(self.user), str(self.achievement))


class AchievementGrantedAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "achievement",
        "achievement_level",
    )

    list_filter = (
        'user',
        'achievement',
    )
