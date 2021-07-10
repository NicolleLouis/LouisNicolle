from achievement.AbstractAchievement import AbstractAchievement
from climax_tracker.repository.profile_repository import ProfileRepository


class LowestAccountAchievement(AbstractAchievement):
    key = 'lowest_account'
    app = 'climax_tracker'
    name = 'Addicted Gambler'

    def __init__(self):
        super().__init__(
            key=self.key,
            app=self.app,
            name=self.name,
        )

    def compute(self, user_profile):
        climax_profile = user_profile.climax_profile
        lowest_profile = ProfileRepository.get_lowest_account()
        if climax_profile.climax_account == lowest_profile.climax_account:
            return True
        return False
