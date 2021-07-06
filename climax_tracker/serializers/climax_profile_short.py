from rest_framework import serializers

from climax_tracker.models.climax_profile import ClimaxProfile


class ClimaxProfileShortSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClimaxProfile
        fields = [
            "id",
            "name",
        ]
