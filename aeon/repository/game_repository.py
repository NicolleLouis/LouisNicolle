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
    def get_by_mage_list(mages_name_list):
        from aeon.repository.mage_repository import MageRepository

        queryset = GameRepository.get_queryset()
        mages = MageRepository.transform_name_list_to_id(mages_name_list)
        if mages_name_list is not None:
            queryset = queryset.filter(mage__in=mages)
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

    @staticmethod
    def get_by_average_ether_cost(average_ether_cost):
        queryset = GameRepository.get_queryset()
        queryset = queryset.filter(average_ether_cost=average_ether_cost)
        return queryset

    @staticmethod
    def get_by_profile(profile):
        queryset = GameRepository.get_queryset()
        queryset = queryset.filter(players=profile)
        return queryset

    @staticmethod
    def filter_by_victory(queryset, is_victory=True):
        return queryset.filter(is_win=is_victory)

    @staticmethod
    def get_nemesis_list(queryset):
        nemesis_list = list(
            set(
                map(
                    lambda game: game.nemesis,
                    queryset
                )
            )
        )
        return nemesis_list

    @staticmethod
    def filter_by_nemesis(queryset, nemesis):
        queryset = queryset.filter(nemesis=nemesis)
        return queryset
