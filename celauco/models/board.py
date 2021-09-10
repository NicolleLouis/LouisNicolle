from celauco.constant.board import CellStatus


class Board:
    height = 9
    width = 9

    def get_state(self, x, y):
        if y < 0 or y >= self.height:
            return CellStatus.ILLEGAL
        if x < 0 or x >= self.width:
            return CellStatus.ILLEGAL
        return CellStatus.EMPTY

    def print(self):
        for y in range(self.height):
            line = ""
            for x in range(self.width):
                line += self.get_state(x, y).value
            print(line)
