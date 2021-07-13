from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from stats.repository.profile_repository import ProfileRepository
from stats.serializers.profile_serializer import ProfileSerializer


class ProfileAchievementView(APIView):
    repository = ProfileRepository
    serializer = ProfileSerializer

    def get(self, request, profile_id, *args, **kwargs):
        profile = self.repository.get_by_id(profile_id)
        profile_serializer = self.serializer(profile)
        data = profile_serializer.data

        return Response(data, status=status.HTTP_200_OK)
