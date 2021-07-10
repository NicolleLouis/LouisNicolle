from climax_tracker.achievements.achievement import achievement_list as list_climax
from aeon.achievements.achievement import achievement_list as list_aeon


class AchievementService:
    @staticmethod
    def get_all_achievements():
        achievement_list = list_climax
        achievement_list.extend(list_aeon)
        return achievement_list
