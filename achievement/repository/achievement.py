from achievement.models.achievement import Achievement


class AchievementRepository:
    @staticmethod
    def get_or_create(key):
        achievement, _created = Achievement.objects.get_or_create(key=key)
        return achievement, _created

    @staticmethod
    def get_by_key(key):
        return Achievement.objects.get(key=key)
