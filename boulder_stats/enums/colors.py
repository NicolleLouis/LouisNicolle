from enum import Enum


class Colors(Enum):
    Orange = 'Orange'
    Green = 'Green'
    Blue = 'Blue'
    Red = 'Red'

    @classmethod
    def choices(cls):
        return [(key.value, key.name) for key in cls]
