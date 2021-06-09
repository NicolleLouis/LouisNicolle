from django.db import models
from django.contrib import admin

from aeon.models.card import Card


class Spell(Card):
    damage = models.IntegerField(
        null=True,
        blank=True
    )
    breach_number = models.IntegerField(
        default=1,
        null=True,
        blank=True,
    )

    class Meta:
        verbose_name = "Spell"
        verbose_name_plural = "Spells"


class SpellAdmin(admin.ModelAdmin):
    list_display = (
        "french_name",
        'ether_cost',
        "is_self_destroyable",
        "damage",
        'breach_number',
    )

    search_fields = [
        'french_name',
        'english_name',
    ]
