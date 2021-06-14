from aeon.repository.nemesis_repository import NemesisRepository
from graph.service.options.linear_axis_service import LinearAxisService
from graph.service.options.option_service import OptionService
from graph.views.line_chart_view import LineChartView
from stats.service.win_rate_service import WinRateService


def nemesis_difficulty_win_rate_view(request):
    view = NemesisDifficultyWinRateView()
    return view.view(request)


class NemesisDifficultyWinRateView(LineChartView):
    def __init__(self):
        super().__init__()
        nemesis_difficulty, difficulty_win_rate = self.split_database_data(
            self.get_database_data()
        )
        self.nemesis_difficulty = nemesis_difficulty
        self.difficulty_win_rate = difficulty_win_rate

    def get_x_labels(self):
        return self.nemesis_difficulty

    def get_data(self):
        return {
            "Win-Rates": self.difficulty_win_rate,
        }

    @staticmethod
    def generate_options():
        options = {}

        y_axis_options = LinearAxisService.get_percentage_y_axis_options()
        OptionService.deep_update(options, y_axis_options)

        x_title_axis_options = LinearAxisService.get_title_x_axis_options("Nemesis Difficulty")
        OptionService.deep_update(options, x_title_axis_options)

        x_linear_axis_options = LinearAxisService.get_x_linear_axis_options()
        OptionService.deep_update(options, x_linear_axis_options)

        x_stepsize_options = LinearAxisService.get_x_tick_step_size_options(1)
        OptionService.deep_update(options, x_stepsize_options)

        return options

    @staticmethod
    def get_database_data():
        difficulty_list = NemesisRepository.get_unique_difficulties()
        nemesis_difficulty_win_rates = []
        for difficulty in difficulty_list:
            nemesis_list = NemesisRepository.get_by_difficulty(difficulty)
            win_rate_service = WinRateService(nemesis_list)
            win_rate = win_rate_service.get_data()
            if win_rate is not None:
                nemesis_difficulty_win_rates.append({
                    "nemesis_difficulty": str(difficulty),
                    "difficulty_win_rate": win_rate
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
        difficulty_win_rate = list(
            map(
                lambda nemesis_data: nemesis_data["difficulty_win_rate"],
                database_data
            )
        )
        return nemesis_difficulty, difficulty_win_rate
