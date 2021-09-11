from enum import Enum


class CellStatus(Enum):
    EMPTY = " "
    HUMAN_HEALTHY = "0"
    HUMAN_INFECTED = "1"
    HUMAN_IMMUNE = "2"
    HUMAN_DEAD = "RIP"
    ILLEGAL = "#"
