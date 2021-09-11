from achievement.abstract_achievement import AbstractAchievement, AbstractAchievementLevel
from achievement.constant.app_list import AppList
from aeon.repository.game_repository import GameRepository


class MageDeathAndVictory(AbstractAchievement):
    key = 'mage_died_and_victory'
    app = AppList.AEON
    name = 'Un sacrifice nécessaire'
    description = 'Gagner une partie en ayant au moins un mage à terre'
    achievement_levels = [
        AbstractAchievementLevel(
            level=1,
            name="A sacrifice I'm willing to make",
            description='1 partie'
        ),
        AbstractAchievementLevel(
            level=2,
            name="The greater good",
            description='10 parties'
        ),
    ]

    def __init__(self):
        super().__init__(
            key=self.key,
            app=self.app,
            name=self.name,
            description=self.description,
            achievement_levels=self.achievement_levels,
        )

    def compute(self, user_profile):
        result = 0
        games_by_player = GameRepository.get_by_profile(user_profile)
        victories_by_player = GameRepository.filter_by_victory(games_by_player)
        victories_with_mage_down = GameRepository.filter_by_at_least_one_mage_died(victories_by_player)
        victories_with_mage_down = victories_with_mage_down.count()
        if victories_with_mage_down > 0:
            result = 1
        if victories_with_mage_down >= 10:
            result = 2
        return result
