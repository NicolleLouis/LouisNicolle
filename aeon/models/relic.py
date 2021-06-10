from django.db import models
from django.contrib import admin

from aeon.models.card import Card


class Relic(Card):
    damage = models.IntegerField(
        null=True,
        blank=True
    )
    ether_win = models.IntegerField(
        null=True,
        blank=True,
    )

    def __str__(self):
        return "Relic: {}".format(self.name())

    class Meta:
        verbose_name = "Relic"
        verbose_name_plural = "Relics"


class RelicAdmin(admin.ModelAdmin):
    list_display = (
        "get_name",
        'ether_cost',
        "is_self_destroyable",
        "damage",
        'ether_win',
    )

    search_fields = [
        'french_name',
        'english_name',
        'extension',
    ]

    list_filter = (
        "extension",
    )

    ordering = (
        "ether_cost",
    )

    autocomplete_fields = ("extension",)

    @staticmethod
    @admin.display(description='name')
    def get_name(instance):
        return str(instance)
