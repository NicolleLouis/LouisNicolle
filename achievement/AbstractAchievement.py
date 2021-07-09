from achievement.models.achievement_level import AchievementLevel
from achievement.repository.achievement import AchievementRepository
from achievement.repository.achievement_granted import AchievementGrantedRepository
from achievement.repository.achievement_level import AchievementLevelRepository


class AbstractAchievementLevel:
    def __init__(self, level, name=None):
        self.level = level
        self.name = name

    def generate(self, achievement):
        achievement_level = AchievementLevel(
            name=self.name,
            level=self.level,
            achievement=achievement
        )
        achievement_level.save()


class AbstractAchievement:
    """
    Argument:
    - key: database id
    - app: app name corresponding to the achievement
    - name: human readable name
    - achievement_levels: list of AbstractAchievementLevel
    """
    def __init__(self, key, app, name, achievement_levels):
        self.key = key
        self.app = app
        self.name = name
        self.achievement_levels = achievement_levels

    def compute(self, user_profile):
        """
        Take a user_profile and should return an integer:
        - 0 if achievement is not reached else the level reached
        """
        raise NotImplementedError("Should implement computation for user_profile")

    def check_achievement(self, user_profile):
        level = self.compute(user_profile)
        if level == 0:
            return
        achievement = AchievementRepository.get_by_key(self.key)
        achievement_level = AchievementLevelRepository.get_by_achievement_and_level(achievement, level)
        achievement_user, created = AchievementGrantedRepository.get_or_create(
            user_profile=user_profile,
            achievement=achievement,
            achievement_level=achievement_level,
        )
        return achievement_user

    def generate(self):
        achievement, _created = AchievementRepository.get_or_create(self.key)
        if not _created:
            return
        achievement.name = self.name
        achievement.app = self.app
        achievement.save()

        for achievement_level in self.achievement_levels:
            print(achievement_level)
            achievement_level.generate(achievement=achievement)
