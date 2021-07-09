from achievement.AbstractAchievement import AbstractAchievement, AbstractAchievementLevel


class ClimaxEatenAchievement(AbstractAchievement):
    key = 'climax_eaten'
    app = 'climax_tracker'
    name = 'Mangeur de climax'
    achievement_levels = [
        AbstractAchievementLevel(
            level=1,
            name="Début de la faim"
        ),
        AbstractAchievementLevel(
            level=2,
            name="Terreur des chinois"
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
        climax_eaten = user_profile.climax_profile.climax_eaten
        if climax_eaten > 0:
            result = 1
        if climax_eaten >= 100:
            result = 2
        return result
