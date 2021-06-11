class Utils:
    @staticmethod
    def ratio_to_percentage(ratio, round_precision=2):
        return round(100 * ratio, round_precision)
