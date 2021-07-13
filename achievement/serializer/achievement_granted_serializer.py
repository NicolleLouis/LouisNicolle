from rest_framework import serializers

from achievement.models.achievement_granted import AchievementGranted


class AchievementGrantedSerializer(serializers.ModelSerializer):

    class Meta:
        model = AchievementGranted
        fields = [
            "id",
            "granted_at",
            'name'
        ]
