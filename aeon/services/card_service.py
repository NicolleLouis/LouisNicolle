from aeon.repository.game_repository import GameRepository
from aeon.services.game_service import GameService


class CardService:
    @staticmethod
    def compute_card_data(card):
        game_queryset = GameRepository.get_all_game_by_card(card=card)
        card.game_number = game_queryset.count()
        win_rate = GameService.get_win_rate(game_queryset)
        if win_rate is not None:
            card.win_rate = win_rate
        card.save()
