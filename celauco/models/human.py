import random

from celauco.models.position import Position


class Human:
    def __init__(self, height, width):
        x = random.randint(0, width - 1)
        y = random.randint(0, height - 1)
        self.position = Position(x, y)

    def get_position(self):
        return self.position

    def __str__(self):
        return "Human on position: {}".format(self.position)
