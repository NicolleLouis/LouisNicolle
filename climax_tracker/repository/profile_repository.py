from climax_tracker.models.climax_profile import ClimaxProfile


class ProfileRepository:
    @staticmethod
    def get_queryset():
        return ClimaxProfile.objects.all()

    @staticmethod
    def get_by_id(profile_id):
        return ClimaxProfile.objects.get(id=profile_id)

    @staticmethod
    def get_lowest_account():
        queryset = ProfileRepository.get_queryset().order_by('climax_account')
        return queryset[0]

    @staticmethod
    def biggest_bet_winner_profile():
        queryset = ProfileRepository.get_queryset().order_by('-total_climax_bet_win')
        return queryset[0]
