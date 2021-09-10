from celauco.constant.human_state import HumanState
from celauco.models.position import Position


class Human:
    state = HumanState.HEALTHY

    # Game variable #
    infection_duration = 10

    def __init__(self, game):
        self.game = game
        self.position = Position.generate_random_position(game.height, game.width)

    def next_turn(self):
        self.move()
        self.update_state()

    def move(self):
        desired_new_position = self.position.get_random_neighbour()
        if self.can_move(desired_new_position):
            self.position = desired_new_position

    def can_move(self, position):
        return self.game.is_cell_empty(position)

    def update_state(self):
        if self.is_infected():
            self.infection_duration += -1
            if self.infection_duration == 0:
                self.set_immune()

    def __str__(self):
        return "Human {} on position: {}".format(self.state.value, self.position)

    def get_position(self):
        return self.position

    def set_infected(self):
        if self.is_healthy():
            self.state = HumanState.INFECTED

    def set_immune(self):
        self.state = HumanState.IMMUNE

    def is_infected(self):
        return self.state == HumanState.INFECTED

    def is_healthy(self):
        return self.state == HumanState.HEALTHY

    def is_immune(self):
        return self.state == HumanState.IMMUNE
