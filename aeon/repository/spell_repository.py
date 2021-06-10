from aeon.models.spell import Spell


class SpellRepository:
    @staticmethod
    def get_queryset():
        return Spell.objects.all()
