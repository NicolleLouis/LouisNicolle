from aeon.models.nemesis import Nemesis


class NemesisRepository:
    @staticmethod
    def get_queryset():
        return Nemesis.objects.all()

    @staticmethod
    def get_unique_difficulties(game_queryset=None):
        nemesis_list = list(
            set(
                map(
                    lambda game: game.nemesis,
                    game_queryset
                )
            )
        )
        difficulty_list = list(
            map(
                lambda nemesis: nemesis.difficulty,
                nemesis_list
            )
        )
        difficulty_list = list(set(difficulty_list))
        return difficulty_list

    @staticmethod
    def get_by_difficulty(difficulty):
        queryset = NemesisRepository.get_queryset()
        queryset = queryset.filter(difficulty=difficulty)
        return queryset

    @staticmethod
    def get_by_name(name):
        return Nemesis.objects.get(english_name=name)

    @staticmethod
    def transform_name_list_to_id(names_list):
        if names_list is None:
            return None
        id_list = list(
            map(
                lambda name: NemesisRepository.get_by_name(name).id,
                names_list
            )
        )
        return id_list
