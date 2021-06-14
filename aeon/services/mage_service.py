from aeon.repository.game_repository import GameRepository
from aeon.services.game_service import GameService


class MageService:
    @staticmethod
    def compute_mage_data(mage):
        game_queryset = GameRepository.get_all_game_by_mage(mage=mage)
        mage.game_number = game_queryset.count()
        win_rate = GameService.get_win_rate(game_queryset)
        if win_rate is not None:
            mage.win_rate = win_rate
        mage.save()
