from aeon.models.nemesis import Nemesis


class NemesisRepository:
    @staticmethod
    def get_queryset():
        return Nemesis.objects.all()
