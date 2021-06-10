from django.db import models
from django.contrib import admin

from aeon.models.card import Card
from aeon.models.mage import Mage
from aeon.models.nemesis import Nemesis
from louis_nicolle.services.model_service import ModelService
from stats.models.profile import Profile


class Game(models.Model):
    id = models.AutoField(primary_key=True)
    mage = models.ManyToManyField(
        Mage,
        blank=True,
    )
    nemesis = models.ForeignKey(
        Nemesis,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
    )
    cards_in_market = models.ManyToManyField(
        Card,
        blank=True,
        help_text="All the available cards",
        verbose_name="Cards",
    )
    players = models.ManyToManyField(
        Profile,
        blank=True,
        help_text="All the human players (Including you)"
    )
    is_win = models.BooleanField(
        default=False,
        verbose_name="Victory",
    )
    number_of_turn = models.IntegerField(
        blank=True,
        null=True,
    )
    date_played = models.DateTimeField(
        auto_now_add=True,
    )

    def __str__(self):
        nemesis = str(self.nemesis) if self.nemesis is not None else 'Unknown Nemesis'
        is_win = "Victory" if self.is_win else "Defeat"
        return "{is_win} against {nemesis} ({date})".format(
            is_win=is_win,
            nemesis=nemesis,
            date=self.date_played,
        )


class GameAdmin(admin.ModelAdmin):
    mandatory_fields = [
        'nemesis',
        'mage',
        'cards_in_market',
        'is_win',
    ]
    hidden_field = [
        "id",
        "date_played",
    ]

    list_display = (
        'nemesis',
        'is_win',
        'number_of_turn',
        'date_played',
    )

    ordering = ["date_played"]

    autocomplete_fields = (
        'nemesis',
        'cards_in_market',
        'mage',
        'players',
    )

    def get_fieldsets(self, request, obj=None):
        all_fields = ModelService.get_model_field_names(Game)
        optional_fields = all_fields
        optional_fields = set(optional_fields) - set(self.mandatory_fields)
        optional_fields = list(optional_fields - set(self.hidden_field))
        optional_fields.sort()
        fieldsets = (
            (None, {
                'fields': self.mandatory_fields
            }),
            ('Optionnal', {
                'fields': optional_fields
            }),
        )
        return fieldsets
