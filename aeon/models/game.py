from django.db import models
from django.contrib import admin
from django.db.models import UniqueConstraint

from aeon.models.card import Card
from aeon.models.mage import Mage
from aeon.models.nemesis import Nemesis


class Game(models.Model):
    id = models.AutoField(primary_key=True)
    cards_in_market = models.ManyToManyField(
        Card,
        blank=True,
    )
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
    number_of_turn = models.IntegerField(
        blank=True,
        null=True
    )
    is_win = models.BooleanField(
        default=False
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
    )
