from aeon.repository.game_repository import GameRepository
from aeon.services.game_service import GameService


class NemesisService:
    @staticmethod
    def compute_nemesis_data(nemesis):
        game_queryset = GameRepository.get_all_game_by_nemesis(nemesis=nemesis)
        nemesis.game_number = game_queryset.count()
        win_rate = GameService.get_win_rate(game_queryset)
        if win_rate is not None:
            nemesis.win_rate = win_rate
        nemesis.save()
