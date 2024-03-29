from achievement.abstract_achievement import AbstractAchievement
from achievement.constant.app_list import AppList
from climax_tracker.repository.profile_repository import ProfileRepository
from stats.models.profile import Profile


class LowestAccountAchievement(AbstractAchievement):
    key = 'lowest_account'
    app = AppList.CLIMAX_TRACKER
    name = 'Addicted Gambler'
    description = 'Perdre un pari et être le joueur le plus en dette'

    def __init__(self):
        super().__init__(
            key=self.key,
            app=self.app,
            name=self.name,
            description=self.description,
        )

    def compute(self, user_profile):
        try:
            climax_profile = user_profile.climax_profile
        except Profile.climax_profile.RelatedObjectDoesNotExist:
            return 0
        lowest_profile = ProfileRepository.get_lowest_account()
        if climax_profile.climax_account == lowest_profile.climax_account:
            return True
        return False
