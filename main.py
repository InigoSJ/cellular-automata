import pygame
from boards.square_tiles import squaredBoard
from utils.extra_funtions import *
from automata.automaton_bases import *
from automata.automaton_functions import *
from automata.neighbour_functions import *
import time


def main():
    WIDTH = 800
    HEIGHT = 800
    BOARD_SIZE_X = 200
    BOARD_SIZE_Y = 200
    PAUSE = 0.1

    BASE_AUTOMATON = base_square_automaton
    AUTOMATON_FUNCTION = day_night_side_corner_automaton

    pygame.init()
    window = pygame.display.set_mode((WIDTH, HEIGHT))

    on = True

    board = squaredBoard(BOARD_SIZE_X, BOARD_SIZE_Y)
    gen = 2

    while on:
        board.draw(WIDTH, HEIGHT, window)
        message_display(f'Generation {gen}', 20, 100, 50, window=window)

        time.sleep(PAUSE)
        board.automaton(BASE_AUTOMATON, AUTOMATON_FUNCTION, gen, alive_needed=[1])
        gen += 1

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.image.save(window, f"screenshots/all_1_2_{gen}.jpg")
                on = False

        pygame.display.update()
        window.fill((0, 0, 0))

    pygame.quit()


if __name__ == "__main__":
    main()
