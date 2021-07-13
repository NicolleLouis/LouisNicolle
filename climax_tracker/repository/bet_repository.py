from climax_tracker.models.bet import Bet


class BetRepository:
    @staticmethod
    def get_queryset():
        return Bet.objects.all().order_by('-created_at')

    @staticmethod
    def get_bet_win_by_profile(profile):
        queryset = BetRepository.get_queryset()
        queryset = queryset.filter(winner=profile)
        return queryset

    @staticmethod
    def get_bet_lost_by_profile(profile):
        queryset = BetRepository.get_queryset()
        queryset = queryset.filter(loser=profile)
        return queryset

    @staticmethod
    def create_bet(
            winner_id,
            loser_id,
            motive,
            climax_amount,
    ):
        from climax_tracker.repository.profile_repository import ProfileRepository

        winner = ProfileRepository.get_by_id(winner_id)
        loser = ProfileRepository.get_by_id(loser_id)
        bet = Bet(
            winner=winner,
            loser=loser,
            climax_amount=climax_amount,
            motive=motive
        )
        bet.save()
