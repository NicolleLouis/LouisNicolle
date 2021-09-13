from django.core.management.base import BaseCommand

from celauco.constant.rooms.cross_room import get_cross_room
from celauco.models.game import Game


class Command(BaseCommand):
    help = 'Try stuff in celauco app'

    def handle(self, *args, **options):
        game = Game(room=get_cross_room(), game_tag="test cécile")
        game.print_board()
        print()
        game.print_state()
        print()

        game.play_game()

        game.print_board()
        print()
        game.print_state()
        print()
