from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from climax_tracker.repository.profile_repository import ProfileRepository
from climax_tracker.serializers.bet import BetSerializer
from climax_tracker.serializers.climax_profile import ClimaxProfileSerializer
from climax_tracker.serializers.pending_bet import PendingBetSerializer


class ProfileDetailView(APIView):
    profile_serializer = ClimaxProfileSerializer
    bet_serializer = BetSerializer
    pending_bet_serializer = PendingBetSerializer
    repository = ProfileRepository

    def get(self, request, profile_id, *args, **kwargs):
        profile = self.repository.get_by_id(profile_id)
        profile_serializer = self.profile_serializer(profile)
        data = profile_serializer.data

        unpaid_bets = profile.get_unpaid_bet()
        unpaid_bets_serializer = self.bet_serializer(unpaid_bets, many=True)
        data["unpaid_bets"] = unpaid_bets_serializer.data

        won_bets = profile.get_won_bets()
        won_bets_serializer = self.bet_serializer(won_bets, many=True)
        data["won_bets"] = won_bets_serializer.data

        pending_bets = profile.get_pending_bets()
        pending_bets_serializer = self.pending_bet_serializer(pending_bets, many=True)
        data["pending_bets"] = pending_bets_serializer.data

        return Response(data, status=status.HTTP_200_OK)
