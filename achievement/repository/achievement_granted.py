from achievement.models.achievement_granted import AchievementGranted


class AchievementGrantedRepository:
    @staticmethod
    def get_or_create(user_profile, achievement, achievement_level):
        achievement_granted, _created = AchievementGranted.objects.get_or_create(
            user=user_profile,
            achievement=achievement,
        )
        achievement_granted.achievement_level = achievement_level
        achievement_granted.save()
        return achievement_granted, _created

    @staticmethod
    def does_achievement_granted_exist(user_profile, achievement, achievement_level):
        try:
            achievement_granted = AchievementGranted.objects.get(
                user=user_profile,
                achievement=achievement,
            )
            if achievement_level == 1:
                return True
            else:
                return achievement_level == achievement_granted.achievement_level.level
        except AchievementGranted.DoesNotExist:
            return False
