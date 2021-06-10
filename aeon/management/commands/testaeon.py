from django.core.management.base import BaseCommand

from aeon.repository.spell_repository import SpellRepository


class Command(BaseCommand):

    def handle(self, *args, **options):
        spells = SpellRepository.get_queryset()
        for spell in spells:
            if spell.breach_number != 1:
                print(spell.name())
                print(spell.breach_number)
