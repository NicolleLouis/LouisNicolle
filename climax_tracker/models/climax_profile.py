from django.db import models
from django.contrib import admin

from climax_tracker.repository.bet_repository import BetRepository
from stats.models.profile import Profile


class ClimaxProfile(models.Model):
    id = models.AutoField(primary_key=True)
    profile = models.ForeignKey(
        Profile,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="profile"
    )
    climax_eaten = models.IntegerField(
        null=True,
        blank=True,
        default=0,
    )
    total_climax_bet_lost = models.IntegerField(
        null=True,
        blank=True,
        default=0,
    )
    total_climax_bet_win = models.IntegerField(
        null=True,
        blank=True,
        default=0,
    )
    climax_account = models.IntegerField(
        null=True,
        blank=True,
        default=0,
    )

    @property
    def name(self):
        return self.profile.name

    def __str__(self):
        return self.name

    def get_unpaid_bet(self):
        lost_bet = BetRepository.get_bet_lost_by_profile(self)
        unpaid_bets = []
        unpaid_bets_climax_amount = 0
        for bet in lost_bet:
            if unpaid_bets_climax_amount + self.climax_account < 0:
                unpaid_bets.append(bet)
                unpaid_bets_climax_amount += bet.climax_amount
        return unpaid_bets


class ClimaxProfileAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'climax_account',
        "climax_eaten",
        "total_climax_bet_lost",
        "total_climax_bet_win",
    )
    readonly_fields = (
        "climax_eaten",
        "climax_account",
        "total_climax_bet_lost",
        "total_climax_bet_win",
    )
