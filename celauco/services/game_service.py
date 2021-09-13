from celauco.models.game_result import GameResult
from celauco.repository.board_repository import BoardRepository


class GameService:
    turn_separator = ","

    @classmethod
    def upload_game_result(cls, game_tag):
        boards = BoardRepository.get_all_boards()
        boards = BoardRepository.order_by_turn_order(boards)
        number_healthy = cls.compute_number_healthy(boards)
        number_immune = cls.compute_number_immune(boards)
        number_infected = cls.compute_number_infected(boards)
        number_of_dead = cls.compute_number_of_dead(boards)
        game_result = GameResult(
            number_healthy=number_healthy,
            number_immune=number_immune,
            number_infected=number_infected,
            number_of_dead=number_of_dead,
            game_tag=game_tag
        )
        game_result.save()

    @classmethod
    def compute_number_healthy(cls, boards):
        number_healthy = ""
        for board in boards:
            number_healthy += "{}{}".format(board.number_healthy, cls.turn_separator)
        number_healthy = number_healthy[:-1]
        return number_healthy

    @classmethod
    def compute_number_immune(cls, boards):
        number_immune = ""
        for board in boards:
            number_immune += "{}{}".format(board.number_immune, cls.turn_separator)
        number_immune = number_immune[:-1]
        return number_immune

    @classmethod
    def compute_number_infected(cls, boards):
        number_infected = ""
        for board in boards:
            number_infected += "{}{}".format(board.number_infected, cls.turn_separator)
        number_infected = number_infected[:-1]
        return number_infected

    @classmethod
    def compute_number_of_dead(cls, boards):
        number_of_dead = ""
        for board in boards:
            number_of_dead += "{}{}".format(board.number_of_dead, cls.turn_separator)
        number_of_dead = number_of_dead[:-1]
        return number_of_dead
