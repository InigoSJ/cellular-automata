import pygame
import numpy as np
from automata.automaton_functions import *
from automata.neighbour_functions import *
from automata.automaton_bases import *


class squaredBoard(object):
    def __init__(self, size_x, size_y):
        self.size_x = size_x
        self.size_y = size_y
        self.board = np.zeros((size_x, size_y))

        self.bound_x = [self.size_x // 2 - 1, self.size_x // 2 + 1]
        self.bound_y = [self.size_y // 2 - 1, self.size_y // 2 + 1]

        self.board[self.size_x // 2][self.size_y // 2] = 1

    def __str__(self):
        board_str = '\n'.join([str(row) for row in self.board])
        return board_str

    def draw(self, board_size_x, board_size_y, window):
        square_size_x, square_size_y = board_size_x / self.size_x, board_size_y / self.size_y

        for y in range(self.size_y):
            for x in range(self.size_x):
                color = [0, 0, 0] if self.board[x][y] == 1 else [255, 255, 255]
                position = (x * square_size_x, y * square_size_y, square_size_x, square_size_y)
                pygame.draw.rect(window, color, position)

    def automaton(self, automaton_base, automaton_fn, gen, alive_needed=[1]):
        self.board, self.bound_x, self.bound_y = automaton_base(self.board, automaton_fn, self.size_x, self.size_y,
                                                                self.bound_x,
                                                                self.bound_y, gen, alive_needed)
