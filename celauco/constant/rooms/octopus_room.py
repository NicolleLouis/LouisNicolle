from celauco.models.position import Position
from celauco.services.room_generator import RoomGeneratorService


def get_octopus_room():
    octopus_room = RoomGeneratorService.generate_empty_room(
        height=9,
        width=9
    )

    walls = [
        Position(x=4, y=0),
        Position(x=4, y=1),
        Position(x=4, y=2),
        Position(x=4, y=3),
        Position(x=4, y=5),
        Position(x=4, y=6),
        Position(x=4, y=7),
        Position(x=4, y=8),
    ]

    RoomGeneratorService.add_walls(octopus_room, walls)
    return octopus_room
