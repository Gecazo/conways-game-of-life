from random import choice

# Size of our field
MAX_SIZE = 10

DEAD_CELL = " "
LIVE_CELL = "*"

def show_field(field):
    for y in range(MAX_SIZE):
        print(''.join(field[y]))

def get_empty_field():
    return [
    [DEAD_CELL for x in range(MAX_SIZE)] for y in range(MAX_SIZE)
]

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
            if c == DEAD_CELL:
                pass
            else:
                pass