from django.core.management.base import BaseCommand

from celauco.constant.rooms.cross_room import get_cross_room
from celauco.models.game import Game


class Command(BaseCommand):
    help = 'Try stuff in celauco app'

    def handle(self, *args, **options):
        number_of_turn = 100
        cross_room = get_cross_room()

        game = Game(room=cross_room)
        game.print_board()
        print()
        game.print_state()
        print()
        for i in range(number_of_turn):
            game.next_turn()
        game.print_board()
        print()
        game.print_state()
        print()
