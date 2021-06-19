from django.core.management.base import BaseCommand

from aeon.repository.game_repository import GameRepository


class Command(BaseCommand):

    def handle(self, *args, **options):
        games = GameRepository.get_queryset()
        for game in games:
            print(game.remaining_nemesis_hp)
