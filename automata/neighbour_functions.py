import numpy as np


def side_neighbours(board, x, y, size_x, size_y):
    alive_neighbours = 0
    if x != size_x - 1:
        alive_neighbours += board[x + 1][y]
    if x != 0:
        alive_neighbours += board[x - 1][y]
    if y != size_y - 1:
        alive_neighbours += board[x][y + 1]
    if y != 0:
        alive_neighbours += board[x][y - 1]
    return alive_neighbours


def corner_neighbours(board, x, y, size_x, size_y):
    alive_neighbours = 0

    if x == 0 and y == 0:
        alive_neighbours += board[x + 1][y + 1]
    elif x == 0 and y == size_y - 1:
        alive_neighbours += board[x + 1][y - 1]
    elif x == size_x - 1 and y == 0:
        alive_neighbours += board[x - 1][y + 1]
    elif x == size_x - 1 and y == size_y - 1:
        alive_neighbours += board[x - 1][y - 1]
    elif x == 0:
        alive_neighbours += board[x + 1][y + 1] + board[x + 1][y - 1]
    elif x == size_x - 1:
        alive_neighbours += board[x - 1][y + 1] + board[x - 1][y - 1]
    elif y == 0:
        alive_neighbours += board[x + 1][y + 1] + board[x - 1][y + 1]
    elif y == size_y - 1:
        alive_neighbours += board[x - 1][y - 1] + board[x + 1][y - 1]
    else:
        alive_neighbours += board[x - 1][y - 1] + board[x + 1][y - 1]
        alive_neighbours += board[x + 1][y + 1] + board[x - 1][y + 1]
    return alive_neighbours


def all_neighbours(board, x, y, size_x, size_y):
    alive_neighbours = 0

    if x == 0 and y == 0:
        alive_neighbours += board[x + 1][y + 1] + board[x + 1][y] + board[x][y + 1]
    elif x == 0 and y == size_y - 1:
        alive_neighbours += board[x + 1][y - 1] + board[x + 1][y] + board[x][y - 1]
    elif x == size_x - 1 and y == 0:
        alive_neighbours += board[x - 1][y + 1] + board[x - 1][y] + board[x][y + 1]
    elif x == size_x - 1 and y == size_y - 1:
        alive_neighbours += board[x - 1][y - 1] + board[x - 1][y] + board[x][y - 1]
    elif x == 0:
        alive_neighbours += board[x + 1][y + 1] + board[x + 1][y - 1] + board[x + 1][y] \
                            + board[x][y + 1] + board[x][y - 1]
    elif x == size_x - 1:
        alive_neighbours += board[x - 1][y + 1] + board[x - 1][y - 1] + board[x - 1][y] \
                            + board[x][y + 1] + board[x][y - 1]
    elif y == 0:
        alive_neighbours += board[x + 1][y + 1] + board[x - 1][y + 1] + board[x + 1][y] \
                            + board[x][y + 1] + board[x - 1][y]
    elif y == size_y - 1:
        alive_neighbours += board[x - 1][y - 1] + board[x + 1][y - 1] + board[x + 1][y] \
                            + board[x][y - 1] + board[x - 1][y]
    else:
        alive_neighbours += board[x - 1][y - 1] + board[x + 1][y - 1] + board[x + 1][y + 1] \
                            + board[x - 1][y + 1] + board[x][y + 1] + board[x][y - 1] \
                            + board[x + 1][y] + board[x - 1][y]
    return alive_neighbours
