from django.db import models
from django.contrib import admin


class GameResult(models.Model):
    id = models.AutoField(primary_key=True)
    game_tag = models.CharField(
        null=True,
        blank=True,
        max_length=22
    )
    number_healthy = models.TextField(
        null=True,
        blank=True,
    )
    number_immune = models.TextField(
        null=True,
        blank=True,
    )
    number_infected = models.TextField(
        null=True,
        blank=True,
    )
    number_of_dead = models.TextField(
        null=True,
        blank=True,
    )


class GameResultAdmin(admin.ModelAdmin):
    list_display = (
        "game_tag",
    )
