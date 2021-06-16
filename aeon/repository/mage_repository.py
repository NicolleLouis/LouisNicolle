from aeon.models.mage import Mage


class MageRepository:
    @staticmethod
    def get_queryset():
        return Mage.objects.all()
