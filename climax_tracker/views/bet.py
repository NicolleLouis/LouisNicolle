from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from climax_tracker.repository.bet_repository import BetRepository


class BetView(APIView):
    repository_class = BetRepository

    def post(self, request, *args, **kwargs):
        """
        data example
        {
            'winner_id': 1,
            'loser_id': 2,
            'motive': 'Louis fait 3 sauts périlleux',
            'climax_amount': '1'
        }
        """
        data = request.data
        self.repository_class.create_bet(
            winner_id=data["winner_id"],
            loser_id=data["loser_id"],
            motive=data["motive"],
            climax_amount=data["climax_amount"],
        )
        return Response({}, status=status.HTTP_200_OK)
