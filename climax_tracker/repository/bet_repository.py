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
