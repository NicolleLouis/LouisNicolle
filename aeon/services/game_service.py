from stats.service.utils import Utils


class GameService:
    @staticmethod
    def get_win_rate(game_queryset):
        number_of_games = game_queryset.count()
        if number_of_games == 0:
            return None
        game_victories = map(
            lambda game: game.is_win,
            game_queryset
        )
        number_of_victories = sum(game_victories)
        victory_ratio = number_of_victories / number_of_games
        return Utils.ratio_to_percentage(victory_ratio)

    @staticmethod
    def update_mage_number(game):
        mages_number = game.mage.all().count()
        game.number_of_mage = mages_number
        game.save()

    @staticmethod
    def update_game_card_info(game):
        from aeon.services.card_service import CardService

        cards = game.cards_in_market.all()
        total_damage = CardService.sum_damage(cards)
        game.total_damage = total_damage
        total_maximum_damage = CardService.sum_maximum_damage(cards)
        game.total_maximum_damage = total_maximum_damage
        game.save()

    @staticmethod
    def compute_average_damage_dealt(games):
        game_number = games.count()
        if game_number == 0:
            return None
        damage_dealt = map(
            lambda game: game.nemesis_damage_dealt if game.nemesis_damage_dealt is not None else 0,
            games
        )
        return sum(damage_dealt) / game_number
