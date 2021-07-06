from rest_framework import serializers

from climax_tracker.models.climax_profile import ClimaxProfile


class ClimaxProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClimaxProfile
        fields = [
            "id",
            "name",
            "climax_eaten",
            "total_climax_bet_lost",
            "total_climax_bet_win",
            "climax_account",
        ]
