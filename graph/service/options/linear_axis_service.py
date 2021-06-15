class LinearAxisService:
    @staticmethod
    def get_percentage_y_axis_options(axis_name="y"):
        return {
            "scales": {
                axis_name: {
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
    def get_title_second_axis(axis_name, axis_title):
        return {
            "scales": {
                axis_name: {
                    "position": "right",
                    'grid': {
                        "display": False,
                    },
                    "title": {
                        "display": True,
                        "text": axis_title,
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

    @staticmethod
    def get_x_linear_axis_options():
        return {
            "scales": {
                "x": {
                    'type': 'linear',
                }
            }
        }

    @staticmethod
    def get_x_tick_step_size_options(step_size):
        return {
            "scales": {
                "x": {
                    "ticks": {
                        "stepSize": step_size
                    }
                }
            }
        }
