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

    @staticmethod
    def get_title_x_axis_options(title):
        return {
            "scales": {
                "x": {
                    "title": {
                        "display": True,
                        "text": title,
                    }
                }
            }
        }
