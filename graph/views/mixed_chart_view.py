from graph.service.color_service import ColorService
from graph.views.chart_view import ChartView


class MixedChartView(ChartView):
    def __init__(self, colors=None):
        super().__init__()
        self.colors = colors
        self.type = None

    def get_colors(self):
        if self.colors is None:
            return ColorService.next_color()
        return ColorService.next_color(self.colors)

    def get_x_labels(self):
        raise NotImplementedError(
            "You should return a labels list for x axe. Exemple: "
            "['Red', 'Blue', 'Yellow', 'Green', 'Purple', 'Orange']"
        )

    def get_data(self):
        raise NotImplementedError(
            """Should return a dict of this type:
            {
                "datasource1": [values_datasource1],
                "datasource2": [values_datasource2],
            }
            """
        )

    @staticmethod
    def get_types(datasource):
        raise NotImplementedError("""Change the type of chart each datasource""")

    @staticmethod
    def get_y_axe_id(datasource):
        """Change the y axis for each datasource"""
        return "y"

    @staticmethod
    def generate_color_option(color):
        color_option = {
            "backgroundColor": "rgba({}, {}, {}, 0.5)".format(*color),
            "borderColor": "rgba({}, {}, {}, 1)".format(*color),
            "pointBackgroundColor": "rgba({}, {}, {}, 1)".format(*color),
            "pointBorderColor": "#fff",
        }
        return color_option

    def generate_dataset(self):
        data = self.get_data()
        if not isinstance(data, dict):
            raise SystemError("Data is faulty")

        color_generator = self.get_colors()
        dataset = []

        for datasource in data:
            new_dataset = {
                "label": datasource,
                "data": data[datasource],
                "type": self.get_types(datasource),
                "yAxisID": self.get_y_axe_id(datasource),
            }
            color = tuple(next(color_generator))
            new_dataset.update(self.generate_color_option(color))
            dataset.append(new_dataset)
        return dataset

    def generate_data(self):
        data = {
            "labels": self.get_x_labels(),
            "datasets": self.generate_dataset(),
        }
        return data
