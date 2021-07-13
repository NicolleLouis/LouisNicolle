from achievement.AbstractAchievement import AbstractAchievement
from achievement.constant.app_list import AppList
from stats.models.profile import Profile


class BiggestBetWinAchievement(AbstractAchievement):
    key = 'biggest_bet_winner'
    app = AppList.CLIMAX_TRACKER
    name = 'King of generosity'
    description = 'Avoir le plus grand nombre de climax gagnés en pari'

    def __init__(self):
        super().__init__(
            key=self.key,
            app=self.app,
            name=self.name,
            description=self.description,
        )

    def compute(self, user_profile):
        from climax_tracker.repository.profile_repository import ProfileRepository

        try:
            climax_profile = user_profile.climax_profile
        except Profile.climax_profile.RelatedObjectDoesNotExist:
            return False
        biggest_bet_winner_profile = ProfileRepository.biggest_bet_winner_profile()
        if climax_profile.total_climax_bet_win == biggest_bet_winner_profile.total_climax_bet_win:
            return True
        return False
