from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from climax_tracker.repository.pending_bet_repository import PendingBetRepository


class PendingBetView(APIView):
    repository_class = PendingBetRepository

    def post(self, request, *args, **kwargs):
        """
        data example
        {
            'player_1_id': 1,
            'player_2_id': 2,
            'motive': 'Louis fait 3 sauts périlleux',
            'climax_amount': '1'
        }
        """
        data = request.data
        self.repository_class.create_pending_bet(
            player_1_id=data["player_1_id"],
            player_2_id=data["player_2_id"],
            motive=data["motive"],
            climax_amount=data["climax_amount"],
        )
        return Response({}, status=status.HTTP_200_OK)
