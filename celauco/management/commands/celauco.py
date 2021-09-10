from django.core.management.base import BaseCommand, CommandError

from celauco.models.game import Game


class Command(BaseCommand):
    help = 'Try stuff in celauco app'

    def handle(self, *args, **options):
        game = Game()
        game.print_board()
        print("#####")
        game.print_state()
        print("#####")
        number_of_turn = 10
        for i in range(number_of_turn):
            game.next_turn()
            game.print_state()
            print("#####")
        game.print_board()
