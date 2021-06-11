from django.http import JsonResponse


class BarChartView:
    def view(self, request):
        return JsonResponse(self.generate_data())

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

    def generate_dataset(self):
        data = self.get_data()
        if not isinstance(data, dict):
            raise SystemError("Data is faulty")
        dataset = []
        for datasource in data:
            dataset.append({
                "label": datasource,
                "data": data[datasource],
            })
        return dataset

    def generate_data(self):
        data = {
            "labels": self.get_x_labels(),
            "datasets": self.generate_dataset(),
        }
        return data
