from django.shortcuts import render

from aeon.repository.game_repository import GameRepository
from aeon.services.game_service import GameService
from graph.service.options.linear_axis_service import LinearAxisService
from graph.service.options.option_service import OptionService
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
    def generate_options():
        options = {}

        y_axis_options = LinearAxisService.get_percentage_y_axis_options()
        OptionService.deep_update(options, y_axis_options)

        second_y_axis_options = LinearAxisService.get_title_second_axis(
            axis_name='y_game_number',
            axis_title='Number of Games',
        )
        OptionService.deep_update(options, second_y_axis_options)

        x_title_axis_options = LinearAxisService.get_title_x_axis_options("Mage Number")
        OptionService.deep_update(options, x_title_axis_options)

        x_linear_axis_options = LinearAxisService.get_x_linear_axis_options()
        OptionService.deep_update(options, x_linear_axis_options)

        x_stepsize_options = LinearAxisService.get_x_tick_step_size_options(1)
        OptionService.deep_update(options, x_stepsize_options)

        return options

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
