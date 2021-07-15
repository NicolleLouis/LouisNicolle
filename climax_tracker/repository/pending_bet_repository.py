from climax_tracker.models.pending_bet import PendingBet


class PendingBetRepository:
    @staticmethod
    def get_queryset():
        return PendingBet.objects.all().order_by('-created_at')

    @staticmethod
    def get_by_id(pending_bet_id):
        return PendingBet.objects.get(id=pending_bet_id)

    @staticmethod
    def create_pending_bet(
            player_1_id,
            player_2_id,
            motive,
            climax_amount,
    ):
        from climax_tracker.repository.profile_repository import ProfileRepository

        player_1 = ProfileRepository.get_by_id(player_1_id)
        player_2 = ProfileRepository.get_by_id(player_2_id)
        pending_bet = PendingBet(
            player_1=player_1,
            player_2=player_2,
            climax_amount=climax_amount,
            motive=motive
        )
        pending_bet.save()
