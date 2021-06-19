from django.contrib import admin

from aeon.models.game import Game
from aeon.services.game_service import GameService
from louis_nicolle.services.model_service import ModelService
from louis_nicolle.services.permission_service import PermissionService


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
        "get_mages_name",
        'is_win',
        'date_played',
    )

    ordering = ["-date_played"]

    autocomplete_fields = (
        'nemesis',
        'cards_in_market',
        'mage',
        'players',
    )

    readonly_fields = (
        "number_of_mage",
        "total_damage",
        "total_maximum_damage"
    )

    actions = (
        "compute_data",
    )

    def get_fieldsets(self, request, obj=None):
        all_fields = ModelService.get_model_field_names(Game)
        optional_fields = all_fields
        optional_fields = set(optional_fields) - set(self.mandatory_fields)
        optional_fields = set(optional_fields) - set(self.readonly_fields)
        optional_fields = list(optional_fields - set(self.hidden_field))
        optional_fields.sort()
        fieldsets = (
            (None, {
                'fields': self.mandatory_fields
            }),
            ('Optional', {
                'fields': optional_fields
            }),
            ('Read-Only', {
                'fields': self.readonly_fields
            }),
        )
        return fieldsets

    def get_changeform_initial_data(self, request):
        return {'players': request.user.profile}

    def get_queryset(self, request):
        aeon = ModelService.get_model_app_name(Game)
        queryset = super(GameAdmin, self).get_queryset(request)
        if PermissionService.is_admin(request.user, aeon):
            return queryset
        return queryset.filter(players=request.user.profile)

    @admin.action(description='Compute Game data', permissions=['change'])
    def compute_data(self, request, queryset):
        for game in queryset:
            GameService.update_mage_number(game)
            GameService.update_game_card_info(game)

    @staticmethod
    def get_mages_name(game):
        mages = game.mage.all()
        mages = list(
            map(
                lambda mage: mage.name,
                mages
            )
        )
        return mages
