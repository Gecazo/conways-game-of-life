import random

# Size of our field
MAX_SIZE = 10

DEAD_CELL = " "
LIVE_CELL = "*"

# Generation
field = []
for i in range(MAX_SIZE):
    for i in range(MAX_SIZE):
        field.append(random.choice([DEAD_CELL, LIVE_CELL]))