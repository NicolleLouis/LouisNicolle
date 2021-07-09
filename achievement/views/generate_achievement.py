from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from climax_tracker.achievements.achievement import achievement_list


class GenerateAchievementView(APIView):
    def post(self, request, *args, **kwargs):
        for achievement in achievement_list:
            achievement.generate()
        return Response({}, status=status.HTTP_201_CREATED)
