from django.db import models
from django.contrib import admin

from achievement.constant.app_list import AppList


class Achievement(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(
        null=True,
        blank=True,
        max_length=50
    )
    key = models.CharField(
        null=True,
        blank=True,
        max_length=50
    )
    app = models.CharField(
        max_length=22,
        choices=AppList.choices,
        default=AppList.AEON,
    )
    description = models.TextField(
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.name


class AchievementAdmin(admin.ModelAdmin):
    list_display = (
        "name",
    )

    search_fields = (
        'name',
        'key',
    )
