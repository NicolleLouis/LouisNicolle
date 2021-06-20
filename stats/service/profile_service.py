from aeon.repository.game_repository import GameRepository


class ProfileService:
    @staticmethod
    def update_profile_data(profile):
        games = GameRepository.get_by_profile(profile)
        profile.game_number = games.count()
        victories = GameRepository.filter_by_victory(games)
        profile.victory_number = victories.count()
        profile.save()
