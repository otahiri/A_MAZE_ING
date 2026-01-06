#!/usr/bin/env python3

import curses as cs
from enum import Enum


class Direction(Enum):
    NORTH = (0, -1, "S")
    SOUTH = (0, 1, "N")
    EAST = (1, 0, "W")
    WEST = (-1, 0, "E")


class Cell:
    def __init__(self) -> None:
        self.sides = {d: True for d in Direction}
        self.grid = [["🭽", "🭶", "🭾"],
                     ["🭰", " ", "🭵"],
                     ["🭼", "🭻", "🭿"]]

    def print_grid(self, cord: list, window: cs.window):
        for y in range(3):
            for x in range(3):
                window.addstr(cord[0] + y, cord[1] + x, self.grid[y][x],)

    def smash_north(self):
        self.grid[0][0] = "🭰"
        self.grid[0][1] = " "
        self.grid[0][2] = "🭵"

    def smash_south(self):
        self.grid[2][0] = "🭰"
        self.grid[2][1] = " "
        self.grid[2][2] = "🭵"

    def smash_west(self):
        self.grid[0][0] = "🭶"
        self.grid[1][0] = " "
        self.grid[2][0] = "🭻"

    def smash_east(self):
        self.grid[0][2] = "🭶"
        self.grid[1][2] = " "
        self.grid[2][2] = "🭻"


def main(window: cs.window):
    height = 9
    width = 9
    maze = [[Cell() for x in range(height)] for y in range(width)]
    for y in range(height):
        for x in range(width):
            maze[y][x].smash_north()
            maze[y][x].print_grid([y * 3, x * 3], window)

    window.refresh()
    window.getch()


cs.wrapper(main)
