from aeon.models.card import Card


class CardRepository:
    @staticmethod
    def get_queryset():
        return Card.objects.all()

    @staticmethod
    def get_card_with_characteristic(characteristic):
        queryset = CardRepository.get_queryset()
        queryset = queryset.filter(**{characteristic: True})
        return queryset
