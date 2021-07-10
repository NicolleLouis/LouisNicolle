from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from climax_tracker.achievements.achievement import achievement_list as list_climax
from aeon.achievements.achievement import achievement_list as list_aeon


class GenerateAchievementView(APIView):
    def post(self, request, *args, **kwargs):
        achievement_list = list_climax
        achievement_list.extend(list_aeon)
        for achievement in achievement_list:
            achievement.generate()
        return Response({}, status=status.HTTP_201_CREATED)
