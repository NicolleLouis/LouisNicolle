from django.core.management.base import BaseCommand, CommandError

from celauco.models.board import Board


class Command(BaseCommand):
    help = 'Try stuff in celauco app'

    def handle(self, *args, **options):
        board = Board()
        board.print()
