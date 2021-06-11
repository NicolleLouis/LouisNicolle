from django.db import models
from django.contrib import admin
from django.db.models import UniqueConstraint

from aeon.constants.card_type import CardType
from aeon.models.extension import Extension
from louis_nicolle.services.model_service import ModelService


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


class CardAdmin(admin.ModelAdmin):
    mandatory_fields = [
        'french_name',
        'english_name',
        'ether_cost',
        'card_type',
        'extension',
    ]
    hidden_fields = [
        "id",
        "game",
    ]
    ether_fields = [
        "ether_gain",
        "ether_maximum_gain",
    ]
    damage_fields = [
        "damage",
        "maximum_damage",
    ]
    heal_fields = [
        "player_heal",
        "gravehold_heal",
    ]
    utility_fields = [
        "is_self_destroyable",
        "has_utility",
        "can_destroy_card",
        "overtime_effect",
    ]

    list_display = (
        "get_name",
        'ether_cost',
        "card_type",
    )

    search_fields = [
        'french_name',
        'english_name',
    ]

    autocomplete_fields = (
        "extension",
    )

    list_filter = (
        "extension",
        "card_type",
    )

    ordering = (
        "ether_cost",
        "card_type",
    )

    @staticmethod
    @admin.display(description='name')
    def get_name(instance):
        return str(instance)

    def get_fieldsets(self, request, obj=None):
        all_fields = ModelService.get_model_field_names(Card)
        other_fields = all_fields
        other_fields = set(other_fields) - set(self.mandatory_fields)
        other_fields = other_fields - set(self.hidden_fields)
        other_fields = other_fields - set(self.damage_fields)
        other_fields = other_fields - set(self.heal_fields)
        other_fields = other_fields - set(self.ether_fields)
        other_fields = list(other_fields - set(self.utility_fields))
        other_fields.sort()
        fieldsets = (
            ('Base', {
                'fields': self.mandatory_fields
            }),
            ('Damage', {
                'fields': self.damage_fields
            }),
            ('Ether', {
                'fields': self.ether_fields
            }),
            ('Heal', {
                'fields': self.heal_fields
            }),
            ('Utility', {
                'fields': self.utility_fields
            }),
            ('Other', {
                'fields': other_fields
            }),
        )
        return fieldsets
