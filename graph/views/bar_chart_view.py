from graph.service.color_service import ColorService
from graph.views.chart_view import ChartView


class BarChartView(ChartView):
    def __init__(self, colors=None):
        super().__init__()
        self.colors = colors
        self.type = "bar"

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
    def generate_color_option(color):
        """Change the color options, you should probably not touch"""
        color_option = {
            "backgroundColor": "rgba({}, {}, {}, 0.5)".format(*color),
            "borderColor": "rgba({}, {}, {}, 1)".format(*color),
            "pointBackgroundColor": "rgba({}, {}, {}, 1)".format(*color),
            "pointBorderColor": "#fff",
        }
        return color_option

    @staticmethod
    def get_y_axe_id(datasource):
        """Change the y axis for each datasource"""
        return "y"

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
                "yAxisID": self.get_y_axe_id(datasource)
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
