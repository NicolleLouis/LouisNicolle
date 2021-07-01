from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from aeon.repository.game_repository import GameRepository
from aeon.services.api_service import ApiService
from aeon.services.game_service import GameService
from graph.service.options.axis_service import AxisService
from graph.views.line_chart_view import LineChartView


class AverageEtherCostData(APIView):
    @staticmethod
    def get(request, *args, **kwargs):
        url_parameters = ["mage"]
        filters = ApiService.extract_parameters_from_url(request, url_parameters)
        graph = AverageEtherCost(filters_mage=filters["mage"])
        return Response(graph.generate_chart(), status=status.HTTP_200_OK)


class AverageEtherCost(LineChartView):
    def __init__(self, filters_mage=None):
        super().__init__()
        average_ether_cost, win_rate = self.split_database_data(
            self.get_database_data(filters_mage)
        )
        self.average_ether_cost = average_ether_cost
        self.win_rate = win_rate
        self.win_rate_datasource = "Win-Rate"
        self.title = "Win-Rate by average card ether cost"

    def get_x_labels(self):
        return self.average_ether_cost

    def get_data(self):
        return {
            self.win_rate_datasource: self.win_rate,
        }

    @staticmethod
    def get_database_data(filters_mage):
        games = GameRepository.get_by_mage_list(filters_mage)
        available_average_ether_cost = list(
            set(
                filter(
                    None,
                    map(
                        lambda game: game.average_ether_cost,
                        games
                    )
                )
            )
        )
        available_average_ether_cost.sort()
        average_ether_cost_win_rate = []
        for average_ether_cost in available_average_ether_cost:
            games = GameRepository.get_by_average_ether_cost(average_ether_cost)
            win_rate = GameService.get_win_rate(games)
            if win_rate is not None:
                average_ether_cost_win_rate.append({
                    "average_ether_cost": average_ether_cost,
                    "win_rate": win_rate,
                })
        return average_ether_cost_win_rate

    @staticmethod
    def split_database_data(database_data):
        average_ether_cost = list(
            map(
                lambda nemesis_data: nemesis_data["average_ether_cost"],
                database_data
            )
        )
        win_rate = list(
            map(
                lambda nemesis_data: nemesis_data["win_rate"],
                database_data
            )
        )
        return average_ether_cost, win_rate

    @staticmethod
    def get_options():
        return [
            AxisService.title_x_axis("Average Ether Cost", size=30),
            AxisService.percentage_y_axis(),
            AxisService.x_linear_axis(),
            AxisService.x_tick_step_size(0.1),
            AxisService.axes_bold_label(axe_id="x", size=15),
            AxisService.axes_bold_label(axe_id="y", size=15),
        ]
