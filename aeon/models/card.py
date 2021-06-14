from django.db import models
from django.db.models import UniqueConstraint

from aeon.constants.card_type import CardType
from aeon.models.extension import Extension


class Card(models.Model):
    id = models.AutoField(primary_key=True)
    french_name = models.CharField(
        null=True,
        blank=True,
        max_length=50
    )
    english_name = models.CharField(
        null=True,
        blank=True,
        max_length=50
    )
    ether_cost = models.IntegerField(
        null=True,
        blank=True
    )
    card_type = models.CharField(
        max_length=7,
        choices=CardType.choices,
        default=CardType.UNKNOWN,
    )
    extension = models.ForeignKey(
        Extension,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
    )
    is_self_destroyable = models.BooleanField(
        default=False
    )
    has_utility = models.BooleanField(
        default=False
    )
    ether_gain = models.IntegerField(
        null=True,
        blank=True
    )
    ether_maximum_gain = models.IntegerField(
        null=True,
        blank=True,
    )
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
    player_heal = models.IntegerField(
        null=True,
        blank=True
    )
    gravehold_heal = models.IntegerField(
        null=True,
        blank=True
    )
    player_maximum_heal = models.IntegerField(
        null=True,
        blank=True
    )
    gravehold_maximum_heal = models.IntegerField(
        null=True,
        blank=True
    )
    breach_focus = models.BooleanField(
        default=False,
    )
    game_number = models.IntegerField(
        null=True,
        blank=True,
    )
    win_rate = models.FloatField(
        null=True,
        blank=True,
    )

    class Meta:
        constraints = [
            UniqueConstraint(fields=['french_name'], name='unique_card_french_name'),
            UniqueConstraint(fields=['english_name'], name='unique_card_english_name')
        ]

    def name(self):
        name = str(self.id)
        if self.french_name is not None:
            name = self.french_name
        if self.english_name is not None:
            name = self.english_name
        return name

    def __str__(self):
        return self.name()
