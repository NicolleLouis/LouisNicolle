from climax_tracker.models.pending_bet import PendingBet


class PendingBetRepository:
    @staticmethod
    def get_queryset():
        return PendingBet.objects.all().order_by('-created_at')

    @staticmethod
    def get_by_id(pending_bet_id):
        return PendingBet.objects.get(id=pending_bet_id)
