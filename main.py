from random import choice

# Size of our field
MAX_SIZE = 10

DEAD_CELL = " "
LIVE_CELL = "*"

def neighbor_xy(x, y):
    for dx, dy in (
        (0, 1),
        (1, 1),
        (1, 0),
        (1, -1),
        (0, -1),
        (-1, -1),
        (-1, 0),
        (-1, 1)
    ):
        yield x + dx, y + dy

def show_field(field):
    for y in range(MAX_SIZE):
        print(''.join(field[y]))

def get_empty_field():
    return [
    [DEAD_CELL for x in range(MAX_SIZE)] for y in range(MAX_SIZE)
]

def if_alive(field, neighbor_x, neighbor_y):
    pass

# Generation
field = [
    [choice([DEAD_CELL, LIVE_CELL]) for x in range(MAX_SIZE)] for y in range(MAX_SIZE)
]

# Pause for next move
while True:
    input('press any key for next step')
    show_field(field)
    buffer = get_empty_field()
    for y in range(MAX_SIZE):
        for x in range(MAX_SIZE):
            с = field[y][x]
            neighbors = 0
            if c == DEAD_CELL:
                for neighbor_x, neighbor_y in neighbor_xy(x, y):
                    neighbors += 1 if is_alive(field,neighbor_x, neighbor_y) else 0
            else:
                pass