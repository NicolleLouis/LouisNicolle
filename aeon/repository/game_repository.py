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

    @staticmethod
    def get_by_mage_number(mage_number):
        queryset = GameRepository.get_queryset()
        queryset = queryset.filter(number_of_mage=mage_number)
        return queryset

    @staticmethod
    def get_by_total_damage(total_damage):
        queryset = GameRepository.get_queryset()
        queryset = queryset.filter(total_damage=total_damage)
        return queryset

    @staticmethod
    def get_by_total_maximum_damage(total_maximum_damage):
        queryset = GameRepository.get_queryset()
        queryset = queryset.filter(total_maximum_damage=total_maximum_damage)
        return queryset
