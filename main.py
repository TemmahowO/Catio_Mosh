import pygame
from pygame.locals import *
import sys
import Functions
import Classes


def main():
    white = [255, 255, 255]
    red = [255, 0, 0]
    gray = [169,169,169]
    black = [0, 0, 0]
    green = [0, 255, 0]
    brown = [150,55,51]

    window_width = 800
    window_height = 700
    fps = 30
    clock = pygame.time.Clock()
    game_on = True

    square_x = 200
    square_y = 200

    window = pygame.display.set_mode((window_width, window_height))
    pygame.display.set_caption("Moshi Game")
    
    player = Classes.Player()

    while game_on:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            
        window.fill(white)
        player.draw(window, black, 20)
        player.player_controller(True, True)
        clock.tick(fps)   
        pygame.display.update()
          


if __name__ == "__main__":
    pygame.init()
    main()
