from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from climax_tracker.repository.profile_repository import ProfileRepository
from climax_tracker.serializers.climax_profile_short import ClimaxProfileShortSerializer


class ProfileView(APIView):
    serializer = ClimaxProfileShortSerializer
    repository = ProfileRepository

    def get(self, request, *args, **kwargs):
        queryset = self.repository.get_queryset()
        serializer = self.serializer(list(queryset), many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
