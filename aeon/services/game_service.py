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
        victory_ratio = number_of_victories/number_of_games
        return Utils.ratio_to_percentage(victory_ratio)

    @staticmethod
    def update_mage_number(game):
        mages_number = game.mage.all().count()
        game.number_of_mage = mages_number
        game.save()
