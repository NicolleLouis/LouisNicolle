from django.http import JsonResponse


class ChartView:
    def __init__(self):
        self.type = None

    def view(self, request):
        return JsonResponse(self.generate_chart())

    def generate_data(self):
        raise NotImplementedError(
            "Data depends on graph type, refers to chart js documentation"
        )

    @staticmethod
    def generate_options():
        return None

    def generate_chart(self):
        chart = {
            "type": self.type,
            "data": self.generate_data(),
            "options": self.generate_options(),
        }
        return chart
