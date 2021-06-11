class LinearAxisService:
    @staticmethod
    def get_percentage_y_axis_options():
        return {
            "scales": {
                "y": {
                    "suggestedMin": 0,
                    "suggestedMax": 100,
                    "title": {
                        "display": True,
                        "text": "Percentage",
                    }
                }
            }
        }
