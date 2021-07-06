from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from climax_tracker.repository.profile_repository import ProfileRepository
from climax_tracker.serializers.bet import BetSerializer
from climax_tracker.serializers.climax_profile import ClimaxProfileSerializer


class ProfileDetailView(APIView):
    profile_serializer = ClimaxProfileSerializer
    bet_serializer = BetSerializer
    repository = ProfileRepository

    def get(self, request, profile_id, *args, **kwargs):
        profile = self.repository.get_by_id(profile_id)
        unpaid_bets = profile.get_unpaid_bet()
        profile_serializer = self.profile_serializer(profile)
        bet_serializer = self.bet_serializer(unpaid_bets, many=True)
        data = profile_serializer.data
        data["unpaid_bets"] = bet_serializer.data
        return Response(data, status=status.HTTP_200_OK)
