from django.http import JsonResponse

from graph.service.color_service import ColorService


class BarChartView:
    def view(self, request):
        return JsonResponse(self.generate_data())

    def get_colors(self, color_list=None):
        if color_list is None:
            return ColorService.next_color()
        return ColorService.next_color(color_list)

    def get_x_labels(self):
        raise NotImplementedError(
            "You should return a labels list ex: "
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

    def generate_color_option(self, color):
        color_option = {
            "backgroundColor": "rgba({}, {}, {}, 0.5)".format(*color),
            "borderColor": "rgba({}, {}, {}, 1)".format(*color),
            "pointBackgroundColor": "rgba({}, {}, {}, 1)".format(*color),
            "pointBorderColor": "#fff",
        }
        return color_option

    def generate_dataset(self):
        data = self.get_data()
        color_generator = self.get_colors()
        if not isinstance(data, dict):
            raise SystemError("Data is faulty")
        dataset = []
        for datasource in data:
            new_dataset = {
                "label": datasource,
                "data": data[datasource],
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
