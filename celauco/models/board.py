from celauco.constant.game import CellStatus

from django.db import models
from django.contrib import admin


class BoardManager(models.Manager):
    """
        Board is used to describe the game board during one turn
        self.board is an array of array describing each cell of the board game
        as a constant from CellStatus
    """
    def create_board(self, board, turn_number=0):
        board_object = self.create(
            turn_number=turn_number
        )
        board_object.set_board(board=board)
        board_object.compute_board_string_representation()
        board_object.compute_values()
        board_object.save()

        return board_object


class Board(models.Model):
    line_separation = "line"
    board = None

    id = models.AutoField(primary_key=True)
    turn_number = models.IntegerField(
        null=True,
        blank=True,
    )
    board_string_representation = models.TextField(
        null=True,
        blank=True,
    )
    number_infected = models.IntegerField(
        null=True,
        blank=True,
    )
    number_healthy = models.IntegerField(
        null=True,
        blank=True,
    )
    number_immune = models.IntegerField(
        null=True,
        blank=True,
    )

    objects = BoardManager()

    def get_state(self, position):
        return self.board[position.y][position.x]

    def set_board(self, board):
        self.board = board

    def compute_board_string_representation(self):
        string_representation = ""
        for line in self.board:
            displayed_line = ""
            for cell in line:
                displayed_line += cell.value
            string_representation += displayed_line
            string_representation += self.line_separation
        self.board_string_representation = string_representation

    def get_height(self):
        return len(self.board)

    def get_width(self):
        return len(self.board[0])

    def compute_values(self):
        self.number_infected = 0
        self.number_healthy = 0
        self.number_immune = 0
        for line in self.board:
            for cell in line:
                if cell == CellStatus.HUMAN_HEALTHY:
                    self.number_healthy += 1
                if cell == CellStatus.HUMAN_INFECTED:
                    self.number_infected += 1
                if cell == CellStatus.HUMAN_IMMUNE:
                    self.number_immune += 1

    def print_board(self):
        for line in self.board:
            displayed_line = ""
            for cell in line:
                displayed_line += cell.value
            print(displayed_line)

    def print_state(self):
        print("Number of human infected: {}".format(self.number_infected))
        print("Number of human healthy: {}".format(self.number_healthy))
        print("Number of human immune: {}".format(self.number_immune))


class BoardAdmin(admin.ModelAdmin):
    list_display = (
        "turn_number",
        "number_healthy",
        "number_infected",
        "number_immune",
    )

    ordering = ("turn_number",)
