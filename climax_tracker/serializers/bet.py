from rest_framework import serializers

from climax_tracker.models.bet import Bet


class BetSerializer(serializers.ModelSerializer):
    winner_name = serializers.SerializerMethodField("get_winner_name")
    loser_name = serializers.SerializerMethodField("get_loser_name")

    class Meta:
        model = Bet
        fields = [
            "id",
            "winner_name",
            "loser_name",
            "climax_amount",
            "motive",
        ]

    @staticmethod
    def get_winner_name(bet):
        return bet.winner.name

    @staticmethod
    def get_loser_name(bet):
        return bet.loser.name
