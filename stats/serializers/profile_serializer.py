from rest_framework import serializers

from stats.models.profile import Profile


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        id = serializers.SerializerMethodField("get_id")
        fields = [
            "id",
            "name",
        ]

        @staticmethod
        def get_id(profile):
            return profile.user.id
