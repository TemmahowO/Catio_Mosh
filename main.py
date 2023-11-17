import pygame
import sys
import Functions
import Classes



def main():
    white = [255, 255, 255]  # Nokky07 was here :0
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

    player = Classes.Player(HP=20, y=300, x=300)
    # test_obj = Classes.Objects()

    while game_on:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        window.fill(white)
        player.draw(window, black)
        player.movement(5)
        Functions.draw_grid(window, red, size=20, no_of_squares=30, 
        max_squares_in_row=2, starting_x=200, starting_y=200)

        clock.tick(fps)
        pygame.display.update()


if __name__ == "__main__":
    pygame.init()
    main()
