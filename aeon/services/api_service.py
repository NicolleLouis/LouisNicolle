class ApiService:
    @staticmethod
    def extract_parameters_from_url(request, parameters):
        extracted_parameters = {}
        for parameter in parameters:
            value = request.GET.get(parameter)
            if value is not None:
                value = value.split(",")
            extracted_parameters[parameter] = value
        return extracted_parameters
