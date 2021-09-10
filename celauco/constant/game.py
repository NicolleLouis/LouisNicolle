from enum import Enum


class CellStatus(Enum):
    EMPTY = "0"
    HUMAN_HEALTHY = "1"
    HUMAN_INFECTED = "#"
    ILLEGAL = "illegal"
