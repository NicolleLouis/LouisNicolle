class AxisService:
    @staticmethod
    def percentage_y_axis(axis_name="y"):
        return {
            "scales": {
                axis_name: {
                    "suggestedMin": 0,
                    "suggestedMax": 100,
                    "title": {
                        "display": True,
                        "text": "Percentage",
                        "font": {
                            "size": 30,
                            "weight": "bold",
                        }
                    }
                }
            }
        }

    @staticmethod
    def title_second_axis(axis_name, axis_title):
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
    def title_x_axis(title, size=12):
        return {
            "scales": {
                "x": {
                    "title": {
                        "display": True,
                        "text": title,
                        "font": {
                            "weight": "bold",
                            "size": size,
                        }
                    }
                }
            }
        }

    @staticmethod
    def x_linear_axis():
        return {
            "scales": {
                "x": {
                    'type': 'linear',
                }
            }
        }

    @staticmethod
    def x_tick_step_size(step_size):
        return {
            "scales": {
                "x": {
                    "ticks": {
                        "stepSize": step_size
                    }
                }
            }
        }

    @staticmethod
    def axes_bold_label(axe_id, size=12):
        return {
            "scales": {
                axe_id: {
                    "ticks": {
                        "font": {
                            "weight": "bold",
                            "size": size,
                        }
                    }
                }
            }
        }
