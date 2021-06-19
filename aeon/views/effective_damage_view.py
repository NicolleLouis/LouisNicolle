from django.shortcuts import render

from aeon.repository.game_repository import GameRepository
from aeon.services.game_service import GameService
from graph.service.options.axis_service import AxisService
from graph.views.line_chart_view import LineChartView


def render_effective_damage_view(request):
    return render(
        request=request,
        template_name='graph/single_graph.html',
        context={
            "title": "Damage Dealt to the Nemesis by available damage in market",
            'data_url': "effective_damage_data",
        }
    )


def effective_damage_data_view(request):
    view = EffectiveDamageView()
    return view.view(request)


class EffectiveDamageView(LineChartView):
    def __init__(self):
        super().__init__()
        damage_available, damage_dealt = self.split_database_data(
            self.get_database_data()
        )
        self.damage_available = damage_available
        self.damage_dealt = damage_dealt
        self.damage_dealt_datasource = "Total damage dealt"

    def get_x_labels(self):
        return self.damage_available

    def get_data(self):
        return {
            self.damage_dealt_datasource: self.damage_dealt,
        }

    @staticmethod
    def get_database_data():
        games = GameRepository.get_queryset()
        available_damage_possibility = list(set(
            map(
                lambda game: game.total_damage,
                games
            )
        ))
        games_available_damage = []
        for available_damage in available_damage_possibility:
            games = GameRepository.get_by_total_damage(available_damage)
            average_damage_dealt = GameService.compute_average_damage_dealt(games)
            if average_damage_dealt is not None:
                games_available_damage.append({
                    "damage_available": available_damage,
                    "damage_dealt": average_damage_dealt,
                })
        return games_available_damage

    @staticmethod
    def split_database_data(database_data):
        damage_available = list(
            map(
                lambda nemesis_data: nemesis_data["damage_available"],
                database_data
            )
        )
        damage_dealt = list(
            map(
                lambda nemesis_data: nemesis_data["damage_dealt"],
                database_data
            )
        )
        return damage_available, damage_dealt

    @staticmethod
    def get_options():
        return [
            AxisService.title_x_axis("Damage Available", size=30),
            AxisService.title_y_axis("Damage Dealt", size=30),
            AxisService.x_linear_axis(),
            AxisService.min_max_y_axis(y_min=0, y_max=70),
            AxisService.x_tick_step_size(1),
            AxisService.axes_bold_label(axe_id="x", size=15),
            AxisService.axes_bold_label(axe_id="y", size=15),
        ]
