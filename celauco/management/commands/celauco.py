from django.core.management.base import BaseCommand

from celauco.constant.rooms.cross_room import get_cross_room
from celauco.models.game import Game
from celauco.repository.board_repository import BoardRepository


class Command(BaseCommand):
    help = 'Try stuff in celauco app'

    def handle(self, *args, **options):
        # BoardRepository.delete_all_boards()

        cross_room = get_cross_room()

        game = Game(room=cross_room)
        game.print_board()
        print()
        game.print_state()
        print()

        game.play_game()

        game.print_board()
        print()
        game.print_state()
        print()
