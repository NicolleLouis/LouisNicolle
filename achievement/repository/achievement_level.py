from achievement.models.achievement_level import AchievementLevel


class AchievementLevelRepository:
    @staticmethod
    def get_by_achievement_and_level(achievement, level):
        try:
            return AchievementLevel.objects.get(
                achievement=achievement,
                level=level
            )
        except AchievementLevel.DoesNotExist:
            return None
