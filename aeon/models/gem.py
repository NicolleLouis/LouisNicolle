from django.db import models
from django.contrib import admin

from aeon.models.card import Card


class Gem(Card):
    ether_gain = models.IntegerField(
        null=True,
        blank=True
    )

    def __str__(self):
        return "Gem: {}".format(self.name())

    class Meta:
        verbose_name = "Gem"
        verbose_name_plural = "Gems"


class GemAdmin(admin.ModelAdmin):
    list_display = (
        "french_name",
        "ether_gain",
        "ether_cost",
        "is_self_destroyable",
    )

    search_fields = [
        'french_name',
        'english_name',
    ]