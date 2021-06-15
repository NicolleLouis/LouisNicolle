from django.db import models
from django.contrib import admin

from aeon.constants.defeat_type import DefeatType
from aeon.constants.victory_type import VictoryType
from aeon.models.card import Card
from aeon.models.mage import Mage
from aeon.models.nemesis import Nemesis
from aeon.services.game_service import GameService
from louis_nicolle.services.model_service import ModelService
from louis_nicolle.services.permission_service import PermissionService
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
        "get_mages_name",
        'is_win',
        'date_played',
    )

    ordering = ["date_played"]

    autocomplete_fields = (
        'nemesis',
        'cards_in_market',
        'mage',
        'players',
    )

    readonly_fields = (
        "number_of_mage",
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
