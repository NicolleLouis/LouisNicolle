from aeon.models.mage import Mage


class MageRepository:
    @staticmethod
    def get_queryset():
        return Mage.objects.all()

    @staticmethod
    def get_by_name(name):
        return Mage.objects.get(english_name=name)

    @staticmethod
    def transform_name_list_to_id(mage_names_list):
        if mage_names_list is None:
            return None
        mage_id_list = list(
            map(
                lambda name: MageRepository.get_by_name(name).id,
                mage_names_list
            )
        )
        return mage_id_list
