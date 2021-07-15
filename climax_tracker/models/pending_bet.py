from django.db import models
from django.contrib import admin


class PendingBet(models.Model):
    id = models.AutoField(primary_key=True)
    player_1 = models.ForeignKey(
        'ClimaxProfile',
        on_delete=models.CASCADE,
        related_name="pending_bet_player_1",
    )
    player_2 = models.ForeignKey(
        'ClimaxProfile',
        on_delete=models.CASCADE,
        related_name="pending_bet_player_2",
    )
    climax_amount = models.IntegerField(
        default=1,
    )
    motive = models.TextField(
        null=True,
        blank=True,
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    def __str__(self):
        return "Pending Bet opposing: {} and {}".format(self.player_1, self.player_2)

    def win(self, player):
        from climax_tracker.models.bet import Bet

        if player not in [self.player_1, self.player_2]:
            raise SystemError("PendingBet should be won by player already registered")
        winner = player
        if winner == self.player_1:
            loser = self.player_2
        else:
            loser = self.player_1

        bet = Bet(
            winner=winner,
            loser=loser,
            climax_amount=self.climax_amount,
            motive=self.motive
        )
        bet.save()
        self.delete()

    def lose(self, player):
        from climax_tracker.models.bet import Bet

        if player not in [self.player_1, self.player_2]:
            raise SystemError("PendingBet should be won by player already registered")
        loser = player
        if loser == self.player_1:
            winner = self.player_2
        else:
            winner = self.player_1

        bet = Bet(
            winner=winner,
            loser=loser,
            climax_amount=self.climax_amount,
            motive=self.motive
        )
        bet.save()
        self.delete()


class PendingBetAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'player_1',
        "player_2",
        'climax_amount',
    )

    list_filter = (
        "player_1",
        "player_2",
    )

    ordering = (
        "-created_at",
    )

    search_fields = (
        "player_1",
        "player_2",
        "motive",
    )
