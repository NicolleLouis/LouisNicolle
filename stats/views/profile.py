from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from stats.repository.profile_repository import ProfileRepository
from stats.serializers.profile_serializer import ProfileSerializer


class ProfileView(APIView):
    serializer = ProfileSerializer
    repository = ProfileRepository

    def get(self, request, *args, **kwargs):
        queryset = self.repository.get_queryset()
        serializer = self.serializer(list(queryset), many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
