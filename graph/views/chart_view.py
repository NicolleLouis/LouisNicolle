from django.http import JsonResponse

from graph.service.options.option_service import OptionService


class ChartView:
    line_type = 'line'
    bar_type = 'bar'

    def __init__(self):
        self.type = None
        self.title = None

    def view(self, request):
        return JsonResponse(self.generate_chart())

    def generate_data(self):
        raise NotImplementedError(
            "Data depends on graph type, refers to chart js documentation"
        )

    @staticmethod
    def get_options():
        """Should return a list of distinct function, all of them will be DeepUpdated"""
        return None

    def generate_options(self):
        """Should probably not override this"""
        option_list = self.get_options()
        if option_list is None:
            return None
        options = {}
        for option in option_list:
            OptionService.deep_update(options, option)
        return options

    def generate_chart(self):
        chart = {
            "data": self.generate_data(),
            "options": self.generate_options(),
        }
        if self.type is not None:
            chart["type"] = self.type
        if self.title is not None:
            chart["title"] = self.title
        return chart
