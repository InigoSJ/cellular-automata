import numpy as np
from .neighbour_functions import *
from .automaton_functions import *


def base_square_automaton(board, automaton_fn, size_x, size_y, bound_x, bound_y, gen, alive_needed=[1]):
    new_board = board.copy()
    for y in range(bound_y[0] - 1, bound_y[1] + 2):
        for x in range(bound_x[0] - 1, bound_x[1] + 2):
            if board[x][y] == 0:
                # Compute neighbours
                alive_neighbours = automaton_fn(board, x, y, size_x, size_y, gen)

                # Compute if alive
                if alive_neighbours in alive_needed:
                    new_board[x][y] = 1
                    # Compute new boundaries
                    if 0 < x < bound_x[0]:
                        bound_x[0] = x
                    if size_x - 1 > x > bound_x[1]:
                        bound_x[1] = x
                    if 0 < y < bound_y[0]:
                        bound_y[0] = y
                    if size_y - 1 > y > bound_y[1]:
                        bound_y[1] = y
    return new_board, bound_x, bound_y
