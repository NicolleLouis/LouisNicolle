from rest_framework import serializers

from stats.models.profile import Profile


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = [
            "name"
        ]
