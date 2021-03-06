from random import choice

# Size of our field
MAX_SIZE = 10

DEAD_CELL = "  "
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

def is_alive(field, neighbor_x, neighbor_y):
    return 0 <= neighbor_x < MAX_SIZE and 0 <= neighbor_y < MAX_SIZE and field[neighbor_x][neighbor_y] == LIVE_CELL

# Generation
field = [
    [choice([DEAD_CELL, LIVE_CELL]) for x in range(MAX_SIZE)] for y in range(MAX_SIZE)
]

# Pause for next move
while True:
    input('press any key for next step ')
    show_field(field)
    buffer = get_empty_field()
    for y in range(MAX_SIZE):
        for x in range(MAX_SIZE):
            c = field[y][x]
            neighbors = 0
            for neighbor_x, neighbor_y in neighbor_xy(x, y):
                    neighbors += 1 if is_alive(field,neighbor_x, neighbor_y) else 0
            if c == DEAD_CELL:
                buffer[y][x] = LIVE_CELL if neighbors == 3 else DEAD_CELL
            else:
                buffer[y][x] = LIVE_CELL if neighbors in (2,3) else DEAD_CELL
    
    #test
    if field == buffer:
        print('stasis')
        break

    field = buffer