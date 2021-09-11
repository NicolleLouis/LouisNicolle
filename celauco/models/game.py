from celauco.constant.game import CellStatus
from celauco.constant.rooms.empty_room import empty_room
from celauco.models.board import Board
from celauco.models.human import Human
from celauco.models.position import Position
from celauco.repository.board_repository import BoardRepository
from celauco.services.probabilty_service import ProbabilityService


class Game:
    humans = []
    boards = []
    room = empty_room
    turn_number = 0

    # Game variable #
    human_number = 30
    infection_probability = 10
    number_of_turn = 50

    def __init__(self, room=None):
        BoardRepository.delete_all_boards()
        if room is not None:
            self.room = room
        self.height = self.room.get_height()
        self.width = self.room.get_width()

        for i in range(self.human_number):
            self.add_human()
        self.humans[0].set_infected()
        self.update_board_history()

    def next_turn(self):
        self.turn_number += 1
        for human in self.humans:
            human.next_turn()
        self.update_infection()
        self.update_board_history()

    def play_game(self):
        for i in range(self.number_of_turn):
            self.next_turn()

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

    def get_room_state(self, position):
        return self.room.get_state(position)

    def get_state(self, position):
        if position.y < 0 or position.y >= self.height:
            return CellStatus.ILLEGAL
        if position.x < 0 or position.x >= self.width:
            return CellStatus.ILLEGAL
        if self.get_room_state(position) == CellStatus.ILLEGAL:
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
        for y in range(self.height):
            line = []
            for x in range(self.width):
                line.append(self.get_state(Position(x=x, y=y)))
            board.append(line)
        return Board.objects.create_board(board=board, turn_number=self.turn_number)

    def print_board(self):
        self.boards[-1].print_board()

    def print_state(self):
        self.boards[-1].print_state()
