from django.shortcuts import render

from aeon.repository.nemesis_repository import NemesisRepository
from graph.service.options.axis_service import AxisService
from graph.views.bar_chart_view import BarChartView


def render_nemesis_win_rate_view(request):
    return render(
        request=request,
        template_name='graph/single_graph.html',
        context={
            "title": "Win-Rate by Nemesis",
            'data_url': "nemesis_win_rate_data",
        }
    )


def nemesis_win_rate_data_view(request):
    view = NemesisWinRateView()
    return view.view(request)


class NemesisWinRateView(BarChartView):
    def __init__(self):
        super().__init__()
        nemesis_names, nemesis_win_rate, game_number = self.split_database_data(
            self.get_database_data()
        )
        self.nemesis_names = nemesis_names
        self.nemesis_win_rate = nemesis_win_rate
        self.game_number = game_number
        self.win_rate_datasource = "Win-Rates"
        self.game_number_datasource = "Game Numbers"

    def get_x_labels(self):
        return self.nemesis_names

    def get_data(self):
        return {
            self.win_rate_datasource: self.nemesis_win_rate,
            self.game_number_datasource: self.game_number
        }

    def get_y_axe_id(self, datasource):
        if datasource == self.game_number_datasource:
            return 'y_game_number'
        return 'y'

    @staticmethod
    def get_database_data():
        nemesis_queryset = NemesisRepository.get_queryset()
        nemesis_win_rates = []
        for nemesis in nemesis_queryset:
            win_rate = nemesis.win_rate
            game_number = nemesis.game_number
            if win_rate is not None:
                nemesis_win_rates.append({
                    "nemesis_name": str(nemesis),
                    "nemesis_win_rate": win_rate,
                    "game_number": game_number,
                })
        nemesis_win_rates.sort(
            key=lambda nemesis_win_rate: nemesis_win_rate["game_number"],
            reverse=True
        )
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
        game_number = list(
            map(
                lambda nemesis_data: nemesis_data["game_number"],
                database_data
            )
        )
        return nemesis_names, nemesis_win_rate, game_number

    @staticmethod
    def get_options():
        return [
            AxisService.percentage_y_axis(),
            AxisService.title_second_axis(
                axis_name='y_game_number',
                axis_title='Number of Games',
            ),
            AxisService.title_x_axis("Nemesis Name", size=30),
            AxisService.axes_bold_label(axe_id="x", size=15),
            AxisService.axes_bold_label(axe_id="y", size=15),
        ]
