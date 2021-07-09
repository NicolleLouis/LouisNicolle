from django.db import models
from django.contrib import admin


class AchievementLevel(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(
        null=True,
        blank=True,
        max_length=50
    )
    level = models.IntegerField(
        default=1
    )
    achievement = models.ForeignKey(
        'Achievement',
        on_delete=models.PROTECT
    )

    def __str__(self):
        return self.name


class AchievementLevelAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "level",
        "achievement",
    )

    search_fields = (
        'name',
    )

    list_filter = (
        "achievement",
    )
