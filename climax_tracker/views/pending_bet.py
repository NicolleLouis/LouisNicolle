from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from climax_tracker.repository.pending_bet_repository import PendingBetRepository
from climax_tracker.repository.profile_repository import ProfileRepository


class PendingBetView(APIView):
    repository_class = PendingBetRepository
    profile_repository = ProfileRepository

    def post(self, request, *args, **kwargs):
        """
        data example
        {
            'pending_bet_id': 1,
            'player_id': 2,
            'is_victory': True,
        }
        """
        data = request.data
        pending_bet = self.repository_class.get_by_id(
            pending_bet_id=data["pending_bet_id"]
        )
        player = self.profile_repository.get_by_id(
            profile_id=data["player_id"]
        )
        is_victory = data["is_victory"]
        if is_victory:
            pending_bet.win(player)
        else:
            pending_bet.lose(player)

        return Response({}, status=status.HTTP_200_OK)
