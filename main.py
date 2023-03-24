import pygame
from pygame.locals import Rect
import sys
import Functions
import Classes
from threading import Thread


def main(debug_mode=False):
    white = [255, 255, 255]  #Nokky07 was here :0
    red = [255, 0, 0]
    gray = [169, 169, 169]
    black = [0, 0, 0]
    green = [0, 255, 0]
    brown = [150, 55, 51]

    window_width = 800
    window_height = 700
    fps = 60
    clock = pygame.time.Clock()
    game_on = True
    temp = 0

    window = pygame.display.set_mode((window_width, window_height))
    pygame.display.set_caption("Moshi Game")

    player = Classes.Player(1)
    # test_obj = Classes.Objects()

    while game_on:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        if debug_mode:
            Functions.debug_mode(player.player_pos.x, player.player_pos.y,
                                 window_width)

        window.fill(white)
        player.draw_hitbox(window, gray, 20)
        player.draw(window, black, 20)
        player.player_controller()
        Functions.draw_grid(window, black, size=50, no_of_squares=4, no_of_rows=0, squares_in_row=2, starting_x=200)

        clock.tick(fps)
        pygame.display.update()


if __name__ == "__main__":
    pygame.init()
    main()
