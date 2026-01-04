#!/usr/bin/env python3

import random as rand
from enum import Enum


class Direction(Enum):
    NORTH = (0, -1, "S")
    SOUTH = (0, 1, "N")
    EAST = (1, 0, "W")
    WEST = (-1, 0, "E")


height = 9
width = 9

rand.seed(input("choose a random seed please"))
maze = [[{d: True for d in Direction} for x in range(height)] for y in range(width)]
bit_maze = []

for row in maze:
    new_row = []
    for cell in row:
        val = 0
        if cell[Direction.NORTH]:
            val |= 1
        if cell[Direction.SOUTH]:
            val |= 2
        if cell[Direction.EAST]:
            val |= 4
        if cell[Direction.WEST]:
            val |= 8
        new_row.append(val)
    bit_maze.append(new_row)
for row in bit_maze:
    print(row)
