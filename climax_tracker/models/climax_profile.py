from django.db import models
from django.contrib import admin

from climax_tracker.repository.bet_repository import BetRepository
from climax_tracker.repository.pending_bet_repository import PendingBetRepository
from stats.models.profile import Profile


class ClimaxProfile(models.Model):
    id = models.AutoField(primary_key=True)
    profile = models.OneToOneField(
        Profile,
        on_delete=models.CASCADE,
        related_name="climax_profile"
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
    created_at = models.DateTimeField(
        auto_now_add=True,
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

    def get_won_bets(self):
        return BetRepository.get_bet_won_by_profile(self)

    def get_pending_bets(self):
        pending_bets = list(PendingBetRepository.get_by_player_1(self))
        pending_bets.extend(list(PendingBetRepository.get_by_player_2(self)))
        return pending_bets


class ClimaxProfileAdmin(admin.ModelAdmin):
    list_display = (
        'id',
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
