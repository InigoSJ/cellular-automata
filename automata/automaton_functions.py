import numpy as np
from .neighbour_functions import *


def day_night_side_corner_automaton(board, x, y, size_x, size_y, gen):
    if gen % 2 == 0:
        alive_neighbours = side_neighbours(board, x, y, size_x, size_y)
    else:
        alive_neighbours = corner_neighbours(board, x, y, size_x, size_y)
    return alive_neighbours


def day_night_side_all_automaton(board, x, y, size_x, size_y, gen):
    if gen % 2 == 0:
        alive_neighbours = side_neighbours(board, x, y, size_x, size_y)
    else:
        alive_neighbours = all_neighbours(board, x, y, size_x, size_y)
    return alive_neighbours


def all_automaton(board, x, y, size_x, size_y, gen):
    return all_neighbours(board, x, y, size_x, size_y)


def summer_winter_automaton(board, x, y, size_x, size_y, gen):
    if gen % 4 < 2:
        alive_neighbours = side_neighbours(board, x, y, size_x, size_y)
    else:
        alive_neighbours = corner_neighbours(board, x, y, size_x, size_y)
    return alive_neighbours


def side_automaton(board, x, y, size_x, size_y, gen):
    return side_neighbours(board, x, y, size_x, size_y)
