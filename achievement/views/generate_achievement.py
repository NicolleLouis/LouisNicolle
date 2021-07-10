from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from achievement.service.achievement_service import AchievementService


class GenerateAchievementView(APIView):
    def post(self, request, *args, **kwargs):
        achievement_list = AchievementService.get_all_achievements()
        for achievement in achievement_list:
            achievement.generate()
        return Response({}, status=status.HTTP_201_CREATED)
