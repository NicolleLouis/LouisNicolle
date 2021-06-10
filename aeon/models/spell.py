from django.db import models
from django.contrib import admin

from aeon.models.card import Card


class Spell(Card):
    damage = models.IntegerField(
        null=True,
        blank=True
    )
    maximum_damage = models.IntegerField(
        null=True,
        blank=True
    )
    breach_number = models.IntegerField(
        default=1,
        null=True,
        blank=True,
    )
    can_destroy_card = models.BooleanField(
        default=False
    )
    overtime_effect = models.BooleanField(
        default=False
    )

    def __str__(self):
        return "Spell: {}".format(self.name())

    class Meta:
        verbose_name = "Spell"
        verbose_name_plural = "Spells"


class SpellAdmin(admin.ModelAdmin):
    list_display = (
        "get_name",
        'ether_cost',
        "damage",
        "maximum_damage",
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
