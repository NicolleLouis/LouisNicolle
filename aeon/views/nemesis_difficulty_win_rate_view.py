from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from aeon.repository.game_repository import GameRepository
from aeon.repository.nemesis_repository import NemesisRepository
from aeon.services.api_service import ApiService
from aeon.services.game_service import GameService
from graph.service.options.axis_service import AxisService
from graph.views.chart_view import ChartView
from graph.views.mixed_chart_view import MixedChartView


class NemesisDifficultyWinRateData(APIView):
    @staticmethod
    def get(request, *args, **kwargs):
        url_parameters = ["mage"]
        filters = ApiService.extract_parameters_from_url(request, url_parameters)
        graph = NemesisDifficultyWinRateGraph(filters_mage=filters["mage"])
        return Response(graph.generate_chart(), status=status.HTTP_200_OK)


class NemesisDifficultyWinRateGraph(MixedChartView):
    def __init__(self, filters_mage=None):
        super().__init__()
        nemesis_difficulty, win_rate, game_number = self.split_database_data(
            self.get_database_data(filters_mage)
        )
        self.nemesis_difficulty = nemesis_difficulty
        self.win_rate = win_rate
        self.game_number = game_number
        self.win_rate_datasource = "Win-Rates"
        self.game_number_datasource = "Game Numbers"

    def get_x_labels(self):
        return self.nemesis_difficulty

    def get_data(self):
        return {
            self.win_rate_datasource: self.win_rate,
            self.game_number_datasource: self.game_number,
        }

    def get_y_axe_id(self, datasource):
        if self.win_rate_datasource == datasource:
            return "y"
        else:
            return "y_game_number"

    @staticmethod
    def get_options():
        return [
            AxisService.percentage_y_axis(),
            AxisService.title_x_axis("Nemesis Difficulty", size=30),
            AxisService.x_linear_axis(),
            AxisService.x_tick_step_size(1),
            AxisService.axes_bold_label(axe_id="x", size=15),
            AxisService.axes_bold_label(axe_id="y", size=15),
            AxisService.title_second_axis(
                axis_name='y_game_number',
                axis_title='Number of Games',
            ),
        ]

    def get_types(self, datasource):
        if datasource == self.win_rate_datasource:
            return ChartView.line_type
        if datasource == self.game_number_datasource:
            return ChartView.bar_type

    @staticmethod
    def get_database_data(filters_mage):
        game_queryset = GameRepository.get_by_mage_list(filters_mage)
        difficulty_list = NemesisRepository.get_unique_difficulties(game_queryset)
        nemesis_difficulty_win_rates = []
        for difficulty in difficulty_list:
            nemesis_list = NemesisRepository.get_by_difficulty(difficulty)
            nemesis_list = NemesisRepository.transform_name_list_to_id(nemesis_list)
            games = GameRepository.filter_by_nemesis(game_queryset, nemesis_list)
            win_rate = GameService.get_win_rate(games)
            game_number = games.count()
            if win_rate is not None:
                nemesis_difficulty_win_rates.append({
                    "nemesis_difficulty": str(difficulty),
                    "win_rate": win_rate,
                    "game_number": game_number
                })
        return nemesis_difficulty_win_rates

    @staticmethod
    def split_database_data(database_data):
        nemesis_difficulty = list(
            map(
                lambda nemesis_data: nemesis_data["nemesis_difficulty"],
                database_data
            )
        )
        win_rate = list(
            map(
                lambda nemesis_data: nemesis_data["win_rate"],
                database_data
            )
        )
        game_number = list(
            map(
                lambda nemesis_data: nemesis_data["game_number"],
                database_data
            )
        )
        return nemesis_difficulty, win_rate, game_number
