from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from achievement.serializer.achievement_granted_serializer import AchievementGrantedSerializer
from stats.repository.profile_repository import ProfileRepository
from stats.serializers.profile_serializer import ProfileSerializer


class ProfileAchievementView(APIView):
    repository = ProfileRepository
    serializer = ProfileSerializer
    achievement_serializer = AchievementGrantedSerializer

    def get(self, request, profile_id, *args, **kwargs):
        profile = self.repository.get_by_id(profile_id)
        profile_serializer = self.serializer(profile)
        data = profile_serializer.data

        achievements = profile.achievements
        achievement_serializer = self.achievement_serializer(achievements, many=True)
        data["achievements"] = achievement_serializer.data

        return Response(data, status=status.HTTP_200_OK)
