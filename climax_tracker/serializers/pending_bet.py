from rest_framework import serializers

from climax_tracker.models.pending_bet import PendingBet


class PendingBetSerializer(serializers.ModelSerializer):
    player_1_name = serializers.SerializerMethodField("get_player_1_name")
    player_2_name = serializers.SerializerMethodField("get_player_2_name")

    class Meta:
        model = PendingBet
        fields = [
            "id",
            "player_1_name",
            "player_2_name",
            "climax_amount",
            "motive",
        ]

    @staticmethod
    def get_player_1_name(pending_bet):
        return pending_bet.player_1.name

    @staticmethod
    def get_player_2_name(pending_bet):
        return pending_bet.player_2.name
