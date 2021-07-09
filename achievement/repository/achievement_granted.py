from achievement.models.achievement_granted import AchievementGranted


class AchievementGrantedRepository:
    @staticmethod
    def get_or_create(user_profile, achievement, achievement_level):
        achievement_user, _created = AchievementGranted.objects.get_or_create(
            user=user_profile,
            achievement=achievement,
        )
        achievement_user.achievement_level = achievement_level
        achievement_user.save()
        return achievement_user, _created
