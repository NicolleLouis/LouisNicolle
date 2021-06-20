from django.shortcuts import render

from aeon.repository.card_repository import CardRepository
from graph.service.options.axis_service import AxisService
from graph.views.radar_chart_view import RadarChartView
from stats.service.win_rate_service import WinRateService


def render_card_characteristic_win_rate_view(request):
    return render(
        request=request,
        template_name='graph/pie_graph.html',
        context={
            "title": "Win-Rate by Nemesis",
            'data_url': "card_characteristic_win_rate_data",
        }
    )


def card_characteristic_win_rate_data_view(request):
    view = NemesisWinRateView()
    return view.view(request)


class NemesisWinRateView(RadarChartView):
    def __init__(self):
        super().__init__()
        self.characteristics = [
            "can_destroy_card",
            "is_self_destroyable",
            "overtime_effect",
            "breach_focus",
            "has_utility",
        ]
        characteristics, card_characteristic_win_rate = self.split_database_data(
            self.get_database_data()
        )
        self.characteristics = characteristics
        self.card_characteristic_win_rate = card_characteristic_win_rate
        self.win_rate_datasource = "Win-Rates"

    def get_x_labels(self):
        return self.characteristics

    def get_data(self):
        return {
            self.win_rate_datasource: self.card_characteristic_win_rate,
        }

    def get_database_data(self):
        card_characteristic_win_rates = []
        for characteristic in self.characteristics:
            cards_with_characteristic = CardRepository.get_card_with_characteristic(characteristic)
            win_rate_service = WinRateService(cards_with_characteristic)
            win_rate, _game_number = win_rate_service.get_data()
            if win_rate is not None:
                card_characteristic_win_rates.append({
                    "characteristics": characteristic,
                    "card_characteristic_win_rate": win_rate,
                })
        return card_characteristic_win_rates

    @staticmethod
    def split_database_data(database_data):
        characteristics = list(
            map(
                lambda nemesis_data: nemesis_data["characteristics"],
                database_data
            )
        )
        card_characteristic_win_rate = list(
            map(
                lambda nemesis_data: nemesis_data["card_characteristic_win_rate"],
                database_data
            )
        )
        return characteristics, card_characteristic_win_rate

    @staticmethod
    def get_options():
        return [
            AxisService.percentage_y_axis("r"),
            AxisService.axes_bold_label(axe_id="r", size=12),
            AxisService.radial_axis_bold_label(size=13),
        ]
