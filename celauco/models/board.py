from celauco.constant.game import CellStatus


class Board:
    """
    Board is used to describe the game board during one turn
    self.board is an array of array describing each cell of the board game as a constant from CellStatus
    """
    number_infected = 0
    number_healthy = 0
    number_immune = 0

    def __init__(self, board):
        self.board = board
        self.compute_values()

    def get_state(self, position):
        return self.board[position.y][position.x]

    def get_height(self):
        return len(self.board)

    def get_width(self):
        return len(self.board[0])

    def compute_values(self):
        number_infected = 0
        number_healthy = 0
        number_immune = 0
        for line in self.board:
            for cell in line:
                if cell == CellStatus.HUMAN_HEALTHY:
                    number_healthy += 1
                if cell == CellStatus.HUMAN_INFECTED:
                    number_infected += 1
                if cell == CellStatus.HUMAN_IMMUNE:
                    number_immune += 1
        self.number_healthy = number_healthy
        self.number_infected = number_infected
        self.number_immune = number_immune

    def print_board(self):
        for line in self.board:
            displayed_line = ""
            for cell in line:
                displayed_line += cell.value
            print(displayed_line)

    def print_state(self):
        print("Number of human infected: {}".format(self.number_infected))
        print("Number of human healthy: {}".format(self.number_healthy))
        print("Number of human immune: {}".format(self.number_immune))
