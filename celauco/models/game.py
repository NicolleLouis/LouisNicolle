from celauco.constant.game import CellStatus
from celauco.models.board import Board
from celauco.models.human import Human
from celauco.models.position import Position
from celauco.services.probabilty_service import ProbabilityService


class Game:
    humans = []
    boards = []

    # Game variable #
    height = 9
    width = 9
    human_number = 20
    infection_probability = 50

    def __init__(self):
        for i in range(self.human_number):
            self.add_human()
        self.humans[0].set_infected()
        self.update_board_history()

    def next_turn(self):
        for human in self.humans:
            human.next_turn()
        self.update_infection()
        self.update_board_history()

    def update_infection(self):
        for human in self.humans:
            if human.is_infected():
                for potential_neighbour in self.humans:
                    if potential_neighbour.is_healthy():
                        if human.position.is_neighbour(potential_neighbour.position):
                            if ProbabilityService.roll_probability(self.infection_probability):
                                potential_neighbour.set_infected()

    def update_board_history(self):
        self.boards.append(self.get_board())

    def get_state(self, position):
        if position.y < 0 or position.y >= self.height:
            return CellStatus.ILLEGAL
        if position.x < 0 or position.x >= self.width:
            return CellStatus.ILLEGAL
        for human in self.humans:
            human_position = human.get_position()
            if human_position.is_equal(position):
                if human.is_healthy():
                    return CellStatus.HUMAN_HEALTHY
                if human.is_infected():
                    return CellStatus.HUMAN_INFECTED
                if human.is_immune():
                    return CellStatus.HUMAN_IMMUNE
        return CellStatus.EMPTY

    def is_cell_empty(self, position):
        return self.get_state(position) == CellStatus.EMPTY

    def add_human(self):
        human = Human(game=self)
        if self.is_cell_empty(human.position):
            self.humans.append(human)

    def get_board(self):
        board = []
        for x in range(self.width):
            line = []
            for y in range(self.width):
                line.append(self.get_state(Position(x, y)))
            board.append(line)
        return Board(board)

    def print_board(self):
        self.boards[-1].print_board()

    def print_state(self):
        self.boards[-1].print_state()
