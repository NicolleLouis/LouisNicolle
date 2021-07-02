from django.db import models
from django.contrib import admin

from climax_tracker.models.climax_profile import ClimaxProfile


class Bet(models.Model):
    id = models.AutoField(primary_key=True)
    winner = models.ForeignKey(
        ClimaxProfile,
        on_delete=models.CASCADE,
        related_name="bet_winner",
    )
    loser = models.ForeignKey(
        ClimaxProfile,
        on_delete=models.CASCADE,
        related_name="bet_loser",
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
        return "{} win {} climax against {}".format(self.winner, self.climax_amount, self.loser)


class BetAdmin(admin.ModelAdmin):
    list_display = (
        'winner',
        "loser",
        'climax_amount',
    )

    list_filter = (
        "winner",
        "loser",
    )

    ordering = (
        "-created_at",
    )

    search_fields = (
        "motive",
    )
