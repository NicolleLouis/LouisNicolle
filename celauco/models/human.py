from celauco.models.position import Position


class Human:
    def __init__(self, height, width, board):
        self.board = board
        self.position = Position.generate_random_position(height, width)

    def get_position(self):
        return self.position

    def __str__(self):
        return "Human on position: {}".format(self.position)

    def can_move(self, position):
        return self.board.is_cell_empty(position)

    def move(self):
        desired_new_position = self.position.get_random_neighbour()
        if self.can_move(desired_new_position):
            self.position = desired_new_position
        else:
            print("Sorry I can't move there")
