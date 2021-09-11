from achievement.models.achievement_level import AchievementLevel
from achievement.repository.achievement import AchievementRepository
from achievement.repository.achievement_granted import AchievementGrantedRepository
from achievement.repository.achievement_level import AchievementLevelRepository


class AbstractAchievementLevel:
    def __init__(self, level, description, name=None):
        self.level = level
        self.description = description
        self.name = name

    def generate(self, achievement):
        achievement_level = AchievementLevel(
            name=self.name,
            level=self.level,
            description=self.description,
            achievement=achievement,
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

    def __init__(self, key, app, name, description, achievement_levels=None):
        self.key = key
        self.app = app
        self.name = name
        self.description = description
        self.achievement_levels = achievement_levels

    @property
    def achievement(self):
        return AchievementRepository.get_by_key(self.key)

    @property
    def maximum_level(self):
        if self.achievement_levels is None:
            return 1
        highest_level = max(
            map(
                lambda achievement_level: achievement_level.level,
                self.achievement_levels
            )
        )
        return highest_level

    def compute(self, user_profile):
        """
        Take a user_profile and should return an integer:
        - 0 if achievement is not reached else the level reached
        """
        raise NotImplementedError("Should implement computation for user_profile")

    def compute_wrapper(self, user_profile):
        computation_result = self.compute(user_profile=user_profile)
        if isinstance(computation_result, int):
            return computation_result
        if isinstance(computation_result, bool):
            if computation_result:
                return 1
            return 0

    def give_achievement(self, user_profile, level):
        achievement = AchievementRepository.get_by_key(self.key)
        achievement_level = AchievementLevelRepository.get_by_achievement_and_level(achievement, level)
        achievement_user, created = AchievementGrantedRepository.get_or_create(
            user_profile=user_profile,
            achievement=achievement,
            achievement_level=achievement_level,
        )
        return achievement_user

    def check_achievement(self, user_profile):
        if self.has_user_reached_maximum_level(user_profile):
            return

        level = self.compute_wrapper(user_profile)
        if level == 0:
            return

        achievement_user = self.give_achievement(
            user_profile=user_profile,
            level=level
        )
        return achievement_user

    def generate(self):
        achievement, _created = AchievementRepository.get_or_create(self.key)
        if not _created:
            return
        achievement.name = self.name
        achievement.app = self.app
        achievement.description = self.description
        achievement.save()

        if self.achievement_levels is not None:
            for achievement_level in self.achievement_levels:
                achievement_level.generate(achievement=achievement)

    def has_user_reached_maximum_level(self, user_profile):
        return AchievementGrantedRepository.does_achievement_granted_exist(
            user_profile=user_profile,
            achievement=self.achievement,
            achievement_level=self.maximum_level,
        )
