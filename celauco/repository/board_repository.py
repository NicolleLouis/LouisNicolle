from celauco.models.board import Board


class BoardRepository:
    @staticmethod
    def delete_all_boards():
        boards = Board.objects.all()
        boards.delete()

    @staticmethod
    def get_all_boards():
        return Board.objects.all()

    @staticmethod
    def order_by_turn_order(queryset):
        queryset.order_by('turn_number')
        return queryset
