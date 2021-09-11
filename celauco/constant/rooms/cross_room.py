from celauco.models.position import Position
from celauco.services.room_generator import RoomGeneratorService


def get_cross_room():
    octopus_room = RoomGeneratorService.generate_empty_room(
        height=9,
        width=9
    )

    walls = [
        Position(x=4, y=0),
        Position(x=4, y=1),
        Position(x=4, y=2),
        Position(x=4, y=6),
        Position(x=4, y=7),
        Position(x=4, y=8),
        ###################
        Position(x=0, y=4),
        Position(x=1, y=4),
        Position(x=2, y=4),
        Position(x=6, y=4),
        Position(x=7, y=4),
        Position(x=8, y=4),
    ]

    RoomGeneratorService.add_walls(octopus_room, walls)
    return octopus_room
