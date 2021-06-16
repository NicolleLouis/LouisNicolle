from django.shortcuts import render

from aeon.repository.game_repository import GameRepository
from aeon.services.game_service import GameService
from graph.service.options.axis_service import AxisService
from graph.views.bar_chart_view import BarChartView


def render_mage_number_win_rate_view(request):
    return render(
        request=request,
        template_name='graph/single_graph.html',
        context={
            "title": "Win-Rate by mages number",
            'data_url': "mage_number_win_rate_data",
        }
    )


def mage_number_win_rate_data_view(request):
    view = MageNumberWinRateView()
    return view.view(request)


class MageNumberWinRateView(BarChartView):
    def __init__(self):
        super().__init__()
        self.possible_mage_number = [1, 2, 3, 4]
        mage_number, win_rate, game_number = self.split_database_data(
            self.get_database_data()
        )
        self.mage_number = mage_number
        self.win_rate = win_rate
        self.game_number = game_number
        self.win_rate_datasource = "Win-Rates"
        self.game_number_datasource = "Game Numbers"

    def get_x_labels(self):
        return self.mage_number

    def get_data(self):
        return {
            self.win_rate_datasource: self.win_rate,
            self.game_number_datasource: self.game_number,
        }

    def get_y_axe_id(self, datasource):
        if datasource == self.game_number_datasource:
            return 'y_game_number'
        return 'y'

    @staticmethod
    def get_options():
        return [
            AxisService.percentage_y_axis(),
            AxisService.title_second_axis(
                axis_name='y_game_number',
                axis_title='Number of Games',
            ),
            AxisService.title_x_axis("Mage Number", size=30),
            AxisService.x_linear_axis(),
            AxisService.x_tick_step_size(1),
            AxisService.axes_bold_label(axe_id="x", size=15),
            AxisService.axes_bold_label(axe_id="y", size=15),
        ]

    def get_database_data(self):
        mage_number_list = self.possible_mage_number
        mage_number_win_rates = []
        for mage_number in mage_number_list:
            games = GameRepository.get_by_mage_number(mage_number)
            win_rate = GameService.get_win_rate(games)
            if win_rate is not None:
                mage_number_win_rates.append({
                    "mage_number": mage_number,
                    "win_rate": win_rate,
                    "game_number": games.count()
                })
        return mage_number_win_rates

    @staticmethod
    def split_database_data(database_data):
        mage_number = list(
            map(
                lambda nemesis_data: nemesis_data["mage_number"],
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
        return mage_number, win_rate, game_number
