from celauco.constant.game import CellStatus
from celauco.models.board import Board


class RoomGeneratorService:
    @staticmethod
    def generate_empty_room(width, height):
        board = []
        for y in range(height):
            line = []
            for x in range(width):
                line.append(CellStatus.EMPTY)
            board.append(line)
        board_object = Board.objects.create_board(board=board)
        return board_object

    @staticmethod
    def add_walls(room, positions):
        print(room)
        for position in positions:
            room.board[position.y][position.x] = CellStatus.ILLEGAL
