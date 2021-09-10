from celauco.constant.board import CellStatus
from celauco.models.human import Human
from celauco.models.position import Position


class Board:
    height = 9
    width = 9
    human_number = 15
    humans = []

    def __init__(self):
        for i in range(self.human_number):
            human = Human(self.height, self.width, self)
            if self.is_cell_empty(human.position):
                self.humans.append(human)
            else:
                print("Could not generate human here")

    def get_state(self, position):
        if position.y < 0 or position.y >= self.height:
            return CellStatus.ILLEGAL
        if position.x < 0 or position.x >= self.width:
            return CellStatus.ILLEGAL
        for human in self.humans:
            human_position = human.get_position()
            if human_position.is_equal(position):
                return CellStatus.HUMAN
        return CellStatus.EMPTY

    def is_cell_empty(self, position):
        return self.get_state(position) == CellStatus.EMPTY

    def next_turn(self):
        for human in self.humans:
            human.move()

    def print(self):
        for y in range(self.height):
            line = ""
            for x in range(self.width):
                line += self.get_state(Position(x, y)).value
            print(line)
        for human in self.humans:
            print(human)
