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
    test_obj = Classes.Objects(HP=1, y=400, x=400)

    while game_on:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_k:
                    print("key pressed")
                    player.hit_points -= 1
                    print(player.hit_points)

        ## Game Logic ##
        if player.hit_points <= 0:
            player.exists = False

        window.fill(white)
        player_rect = player.draw(window, black)
        obj_rect = test_obj.draw(window, brown)

        if Functions.collision_check(player_rect, obj_rect):
            player.check_for_input = False
        else:
            player.check_for_input = True


        Functions.draw_text(window, size=50, 
        text=f"Health: {player.hit_points}", colour=red, coords=(30, 30))
        player.movement(5)
        #Functions.draw_grid(window, red, size=20, no_of_squares=30, 
       # max_squares_in_row=2, starting_x=200, starting_y=200)

        clock.tick(fps)
        pygame.display.update()


if __name__ == "__main__":
    pygame.init()
    main()
