from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from aeon.repository.mage_repository import MageRepository
from aeon.serializers.mage_serializer import MageSerializer


class MageView(APIView):
    serializer = MageSerializer
    repository = MageRepository

    def get(self, request, *args, **kwargs):
        queryset = self.repository.get_mage_played()
        serializer = self.serializer(list(queryset), many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
