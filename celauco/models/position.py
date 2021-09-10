import random


class Position:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return '({},{})'.format(self.x, self.y)

    @staticmethod
    def generate_random_position(height, width):
        x = random.randint(0, width - 1)
        y = random.randint(0, height - 1)
        return Position(x, y)

    def is_equal(self, position):
        if position.x != self.x:
            return False
        if position.y != self.y:
            return False
        return True

    def get_neighbours(self):
        neighbours = [
            Position(self.x + 1, self.y),
            Position(self.x - 1, self.y),
            Position(self.x, self.y + 1),
            Position(self.x, self.y - 1),
        ]
        return neighbours

    def get_random_neighbour(self):
        neighbours = self.get_neighbours()
        return random.choice(neighbours)

    def is_neighbour(self, position):
        neighbours = self.get_neighbours()
        for neighbour in neighbours:
            if neighbour.is_equal(position):
                return True
        return False
