import random


class Human:
    x = 0
    y = 0

    def __init__(self, height, width):
        self.x = random.randint(0, width - 1)
        self.y = random.randint(0, height - 1)

    def get_position(self):
        return self.x, self.y

    def print(self):
        print("Human on position: ({}, {})".format(self.x, self.y))
