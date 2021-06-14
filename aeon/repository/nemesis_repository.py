from aeon.models.nemesis import Nemesis


class NemesisRepository:
    @staticmethod
    def get_queryset():
        return Nemesis.objects.all()

    @staticmethod
    def get_unique_difficulties():
        nemesis_queryset = NemesisRepository.get_queryset()
        difficulty_list = list(
            map(
                lambda nemesis: nemesis.difficulty,
                nemesis_queryset
            )
        )
        difficulty_list = list(set(difficulty_list))
        return difficulty_list

    @staticmethod
    def get_by_difficulty(difficulty):
        queryset = NemesisRepository.get_queryset()
        queryset = queryset.filter(difficulty=difficulty)
        return queryset
