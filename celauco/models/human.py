from celauco.constant.human_state import HumanState
from celauco.models.position import Position


class Human:
    def __init__(self, height, width, game):
        self.game = game
        self.position = Position.generate_random_position(height, width)
        self.state = HumanState.HEALTHY

    def __str__(self):
        return "Human on position: {}".format(self.position)

    def get_position(self):
        return self.position

    def set_infected(self):
        self.state = HumanState.INFECTED

    def is_infected(self):
        return self.state == HumanState.INFECTED

    def is_healthy(self):
        return self.state == HumanState.HEALTHY

    def can_move(self, position):
        return self.game.is_cell_empty(position)

    def move(self):
        desired_new_position = self.position.get_random_neighbour()
        if self.can_move(desired_new_position):
            self.position = desired_new_position
