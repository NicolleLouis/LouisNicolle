from aeon.repository.game_repository import GameRepository
from aeon.repository.nemesis_repository import NemesisRepository
from aeon.services.game_service import GameService
from graph.service.options.linear_axis_service import LinearAxisService
from graph.views.bar_chart_view import BarChartView


def nemesis_win_rate_view(request):
    view = NemesisWinRateView()
    return view.view(request)


class NemesisWinRateView(BarChartView):
    def __init__(self):
        super().__init__()
        nemesis_names, nemesis_win_rate = self.split_database_data(
            self.get_database_data()
        )
        self.nemesis_names = nemesis_names
        self.nemesis_win_rate = nemesis_win_rate

    def get_x_labels(self):
        return self.nemesis_names

    def get_data(self):
        return {
            "Win-Rates": self.nemesis_win_rate,
        }

    @staticmethod
    def generate_options():
        options = {}

        y_axis_options = LinearAxisService.get_percentage_y_axis_options()
        options.update(y_axis_options)
        return options

    @staticmethod
    def get_database_data():
        nemesis_queryset = NemesisRepository.get_queryset()
        nemesis_win_rates = []
        for nemesis in nemesis_queryset:
            win_rate = nemesis.win_rate
            if win_rate is not None:
                nemesis_win_rates.append({
                    "nemesis_name": str(nemesis),
                    "nemesis_win_rate": win_rate
                })
        return nemesis_win_rates

    @staticmethod
    def split_database_data(database_data):
        nemesis_names = list(
            map(
                lambda nemesis_data: nemesis_data["nemesis_name"],
                database_data
            )
        )
        nemesis_win_rate = list(
            map(
                lambda nemesis_data: nemesis_data["nemesis_win_rate"],
                database_data
            )
        )
        return nemesis_names, nemesis_win_rate
