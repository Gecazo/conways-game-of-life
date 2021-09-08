from random import choice

# Size of our field
MAX_SIZE = 10

DEAD_CELL = " "
LIVE_CELL = "*"

def show_field(field):
    for y in range(MAX_SIZE):
        print(''.join(field[y]))

# Generation
field = [
    [choice([DEAD_CELL, LIVE_CELL]) for x in range(MAX_SIZE)] for y in range(MAX_SIZE)
]

# Pause for next move
while True:
    input('press any key for next step')
    show_field(field)