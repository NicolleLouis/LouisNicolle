from achievement.AbstractAchievement import AbstractAchievement, AbstractAchievementLevel
from aeon.repository.game_repository import GameRepository


class MageDeathAndVictory(AbstractAchievement):
    key = 'mage_died_and_victory'
    app = 'aeon'
    name = 'Un sacrifice nécessaire'
    achievement_levels = [
        AbstractAchievementLevel(
            level=1,
            name="A sacrifice I'm willing to make"
        ),
        AbstractAchievementLevel(
            level=2,
            name="The greater good"
        ),
    ]

    def __init__(self):
        super().__init__(
            key=self.key,
            app=self.app,
            name=self.name,
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
