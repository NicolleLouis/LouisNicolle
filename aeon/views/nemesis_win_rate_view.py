from graph.views.bar_chart_view import BarChartView


class NemesisWinRateView(BarChartView):
    def get_x_labels(self):
        return ["Nemesis1", "Nemesis2", "Nemesis3"]

    def get_data(self):
        return {
                "winrate": [100, 25, 64],
            }
