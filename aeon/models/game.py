from django.db import models

from aeon.constants.defeat_type import DefeatType
from aeon.constants.difficulty_type import DifficultyType
from aeon.constants.victory_type import VictoryType
from aeon.models.card import Card
from aeon.models.mage import Mage
from aeon.models.nemesis import Nemesis
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
    victory_type = models.CharField(
        max_length=19,
        choices=VictoryType.choices,
        default=VictoryType.UNKNOWN,
    )
    defeat_type = models.CharField(
        max_length=22,
        choices=DefeatType.choices,
        default=DefeatType.UNKNOWN,
    )
    nemesis_hit_point = models.IntegerField(
        blank=True,
        null=True,
        verbose_name="Nemesis HP",
    )
    gravehold_hit_point = models.IntegerField(
        blank=True,
        null=True,
        verbose_name="Gravehold HP",
    )
    mages_hit_point = models.IntegerField(
        blank=True,
        null=True,
        verbose_name="Total Mage HP",
    )
    number_of_exhausted_mage = models.IntegerField(
        blank=True,
        null=True,
        verbose_name="Total number of mage exhausted",
    )
    number_of_mage = models.IntegerField(
        blank=True,
        null=True,
    )
    game_difficulty = models.CharField(
        max_length=8,
        choices=DifficultyType.choices,
        default=DifficultyType.STANDARD,

    )
    date_played = models.DateTimeField(
        auto_now_add=True,
    )
    total_damage = models.IntegerField(
        blank=True,
        null=True,
    )
    total_maximum_damage = models.IntegerField(
        blank=True,
        null=True,
    )

    @property
    def nemesis_damage_dealt(self):
        if self.nemesis_hit_point is None:
            return None
        if self.nemesis.total_hp is None:
            return None
        return self.nemesis.total_hp - self.nemesis_hit_point

    def __str__(self):
        nemesis = str(self.nemesis) if self.nemesis is not None else 'Unknown Nemesis'
        is_win = "Victory" if self.is_win else "Defeat"
        return "{is_win} against {nemesis} ({date})".format(
            is_win=is_win,
            nemesis=nemesis,
            date=self.date_played,
        )
