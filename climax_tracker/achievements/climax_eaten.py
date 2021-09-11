from achievement.abstract_achievement import AbstractAchievement, AbstractAchievementLevel
from achievement.constant.app_list import AppList
from stats.models.profile import Profile


class ClimaxEatenAchievement(AbstractAchievement):
    key = 'climax_eaten'
    app = AppList.CLIMAX_TRACKER
    name = 'Mangeur de climax'
    description = 'Manger un certain nombre de climax'
    achievement_levels = [
        AbstractAchievementLevel(
            level=1,
            name="Début de la faim",
            description='1 climax',
        ),
        AbstractAchievementLevel(
            level=2,
            name="Terreur des chinois",
            description='100 climax',
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
        try:
            climax_profile = user_profile.climax_profile
        except Profile.climax_profile.RelatedObjectDoesNotExist:
            return 0
        climax_eaten = climax_profile.climax_eaten
        if climax_eaten > 0:
            result = 1
        if climax_eaten >= 100:
            result = 2
        return result
