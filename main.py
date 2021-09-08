from random import choice

# Size of our field
MAX_SIZE = 10

DEAD_CELL = " "
LIVE_CELL = "*"

# Generation
field = [
    [choice([DEAD_CELL, LIVE_CELL]) for x in range(MAX_SIZE)] for y in range(MAX_SIZE)
]

print(field)