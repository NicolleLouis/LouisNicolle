import itertools

from graph.service.color_service import ColorService
from graph.views.chart_view import ChartView


class PieChartView(ChartView):
    def __init__(self, field_name=None, colors=None):
        super().__init__()
        self.field_name = field_name
        self.colors = colors
        self.type = "doughnut"

    def get_colors(self):
        """Change color function, you should probably just change the color range in init"""
        if self.colors is None:
            return ColorService.next_color()
        return ColorService.next_color(self.colors)

    def get_x_labels(self):
        """Change the X labels"""
        raise NotImplementedError(
            "You should return a labels list ex: "
            "['Red', 'Blue', 'Yellow', 'Green', 'Purple', 'Orange']"
        )

    def get_data(self):
        """Change the graph data"""
        raise NotImplementedError(
            """Should return a dict of this type:
            {
                "datasource1": [values_datasource1],
                "datasource2": [values_datasource2],
            }
            """
        )

    @staticmethod
    def generate_color_option(colors):
        """Change the color options, you should probably not touch"""
        color_background = list(
            map(
                lambda color: "rgba({}, {}, {}, 0.5)".format(*color),
                colors
            )
        )
        color_option = {
            "backgroundColor": color_background,
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
            }
            colors = list(itertools.islice(color_generator, len(data[datasource])))
            new_dataset.update(self.generate_color_option(colors))
            dataset.append(new_dataset)
        return dataset

    def generate_data(self):
        data = {
            "labels": self.get_x_labels(),
            "datasets": self.generate_dataset(),
        }
        return data
