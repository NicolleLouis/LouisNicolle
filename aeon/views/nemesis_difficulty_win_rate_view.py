from django.shortcuts import render
from aeon.repository.nemesis_repository import NemesisRepository
from graph.service.options.axis_service import AxisService
from graph.views.line_chart_view import LineChartView
from stats.service.win_rate_service import WinRateService


def render_nemesis_difficulty_win_rate_view(request):
    return render(
        request=request,
        template_name='graph/single_graph.html',
        context={
            "title": "Win-Rate by Nemesis Difficulty",
            'data_url': "nemesis_difficulty_win_rate_data",
        }
    )


def nemesis_difficulty_win_rate_data_view(request):
    view = NemesisDifficultyWinRateView()
    return view.view(request)


class NemesisDifficultyWinRateView(LineChartView):
    def __init__(self):
        super().__init__()
        nemesis_difficulty, win_rate = self.split_database_data(
            self.get_database_data()
        )
        self.nemesis_difficulty = nemesis_difficulty
        self.win_rate = win_rate

    def get_x_labels(self):
        return self.nemesis_difficulty

    def get_data(self):
        return {
            "Win-Rates": self.win_rate,
        }

    @staticmethod
    def get_options():
        return [
            AxisService.percentage_y_axis(),
            AxisService.title_x_axis("Nemesis Difficulty", size=30),
            AxisService.x_linear_axis(),
            AxisService.x_tick_step_size(1),
            AxisService.axes_bold_label(axe_id="x", size=15),
            AxisService.axes_bold_label(axe_id="y", size=15),
        ]

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
                    "win_rate": win_rate
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
        return nemesis_difficulty, win_rate
