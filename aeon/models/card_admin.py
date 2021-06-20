from django.contrib import admin

from aeon.models.card import Card
from aeon.services.card_service import CardService
from louis_nicolle.services.model_service import ModelService


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
        "player_maximum_heal",
        "gravehold_heal",
        "gravehold_maximum_heal",
    ]
    utility_fields = [
        "is_self_destroyable",
        "has_utility",
        "can_destroy_card",
        "overtime_effect",
        "breach_focus",
    ]

    list_display = (
        "name",
        'ether_cost',
        "game_number",
        "win_rate",
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

    readonly_fields = (
        "game_number",
        "win_rate",
    )

    actions = (
        "compute_data",
    )

    def get_fieldsets(self, request, obj=None):
        all_fields = ModelService.get_model_field_names(Card)
        other_fields = all_fields
        other_fields = set(other_fields) - set(self.mandatory_fields)
        other_fields = other_fields - set(self.hidden_fields)
        other_fields = other_fields - set(self.damage_fields)
        other_fields = other_fields - set(self.heal_fields)
        other_fields = other_fields - set(self.ether_fields)
        other_fields = other_fields - set(self.readonly_fields)
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
            ('Read-Only', {
                'fields': self.readonly_fields
            }),
        )
        return fieldsets

    @admin.action(description='Compute Card data', permissions=['change'])
    def compute_data(self, request, queryset):
        for card in queryset:
            CardService.compute_card_data(card)
