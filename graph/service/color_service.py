from graph.constants.color import COLORS


class ColorService:
    @staticmethod
    def next_color(color_list=COLORS):
        for color in color_list:
            yield color
