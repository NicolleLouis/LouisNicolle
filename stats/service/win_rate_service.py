class WinRateService:
    """
    Service computing the win rate of a list of objects.

    Each object should have 2 properties:
    - game_number
    - win-rate
    """

    needed_fields = [
        "game_number",
        "win_rate",
    ]

    def __init__(self, list_object):
        self.list_object = list_object
        self.total_game_number = 0
        self.total_win_rate = None
        self.is_list_valid()
        self.compute_total_win_rate()

    def get_data(self):
        if self.total_win_rate is None:
            return None
        return round(self.total_win_rate, 2)

    def compute_total_win_rate(self):
        for object in self.list_object:
            self.add_object(object)

    def add_object(self, object):
        if object.game_number == 0 or object.win_rate is None:
            return
        if self.total_game_number == 0:
            self.total_game_number = object.game_number
            self.total_win_rate = object.win_rate
        else:
            self.total_win_rate = (self.total_game_number * self.total_win_rate
                                   + object.game_number * object.win_rate)\
                                  / (self.total_game_number + object.game_number)
            self.total_game_number = self.total_game_number + object.game_number

    def is_list_valid(self):
        for object in self.list_object:
            for needed_field in self.needed_fields:
                if not hasattr(object, needed_field):
                    raise SystemError("Object didn't have needed fields")
