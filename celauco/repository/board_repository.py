from celauco.models.board import Board


class BoardRepository:
    @staticmethod
    def delete_all_boards():
        boards = Board.objects.all()
        boards.delete()
