from aeon.models.game import Game


class GameRepository:
    @staticmethod
    def get_queryset():
        return Game.objects.all()

    @staticmethod
    def get_all_game_by_nemesis(nemesis):
        queryset = GameRepository.get_queryset()
        queryset = queryset.filter(nemesis=nemesis)
        return queryset

    @staticmethod
    def get_all_game_by_mage(mage):
        queryset = GameRepository.get_queryset()
        queryset = queryset.filter(mage=mage)
        return queryset

    @staticmethod
    def get_all_game_by_card(card):
        queryset = GameRepository.get_queryset()
        queryset = queryset.filter(cards_in_market=card)
        return queryset
