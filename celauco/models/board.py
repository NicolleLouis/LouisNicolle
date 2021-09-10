from celauco.constant.board import CellStatus
from celauco.models.human import Human


class Board:
    height = 9
    width = 9
    human_number = 9
    humans = []

    def __init__(self):
        for i in range(self.human_number):
            self.humans.append(Human(self.height, self.width))

    def get_state(self, x, y):
        if y < 0 or y >= self.height:
            return CellStatus.ILLEGAL
        if x < 0 or x >= self.width:
            return CellStatus.ILLEGAL
        for human in self.humans:
            human_x, human_y = human.get_position()
            if x == human_x and y == human_y:
                return CellStatus.HUMAN
        return CellStatus.EMPTY

    def print(self):
        for y in range(self.height):
            line = ""
            for x in range(self.width):
                line += self.get_state(x, y).value
            print(line)
        for human in self.humans:
            human.print()
