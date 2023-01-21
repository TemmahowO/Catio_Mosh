import pygame
from pygame.locals import *
import sys
from Classes import * 
import Functions


def main():
    pygame.init()

    white = [255, 255, 255]
    red = [255, 0, 0]
    gray = [169,169,169]
    black = [0, 0, 0]
    green = [0, 255, 0]
    brown = [150,55,51]

    window_width = 800
    window_height = 700
    fps = 60
    clock = pygame.time.Clock()
    Game_on = True
    draw_food = False
    draw_wood = False
    raw_food_count = 0
    wood_count = 0

    player = Player(10)
    tree = Object(5, 20)
    food = Object(1, 5)
    wood = Object(1, 10)


    window = pygame.display.set_mode((window_width, window_height))
    pygame.display.set_caption("Moshi Game")

    while Game_on == True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Game_on = False
                
            if event.type == pygame.KEYDOWN:
                if raw_food_count <= 0:
                    pass
                elif event.key == K_e or event.key == K_q:
                    player.hunger += food.saturation
                    raw_food_count -= 1


            if pygame.mouse.get_pressed() == (1, 0, 0) and Rect.colliderect(player.hitbox_rect, tree.rect):
                red[0] -= 5
                tree.durability -= 0.5
                if tree.durability <= 0:
                    food.x_pos = tree.x_pos + tree.size /2
                    food.y_pos = tree.y_pos + tree.size /2
                    wood.x_pos = tree.x_pos + tree.size /2 - 20
                    wood.y_pos = tree.y_pos + tree.size /2 - 20
                    draw_food = True
                    draw_wood = True
                    tree.randomize_coords(window, red, 20) # Arguments are there because the draw method is called within the randomize_coords method.
                    tree.durability = 10
                    red[0] = 255
                # Prevents an exception.
                if red[0] <= 0:
                    red[0] = 255

        # Collision detection
        if Rect.colliderect(player.rect, food.rect):
            draw_food = False
            raw_food_count += 1
            food.x_pos = 99999
            food.draw(window, green, 5) # Updates the rectangles position
        elif Rect.colliderect(player.rect, wood.rect):
            draw_wood = False
            wood_count += 1
            wood.x_pos = 99999
            wood.draw(window, green, 5) # Updates the rectangles position


        # Functions.keybinds(player, food.saturation, raw_food_count)
        window.fill(gray)
        player.draw_hitbox(window, gray, 10) # hitbox
        player.draw(window, black, 10) # player
        tree.draw(window, red, 20)
        if draw_food == True:
            food.draw(window, green, 5)
        if draw_wood == True:
            wood.draw(window, brown, 10)
        
        # Drawing text
        Functions.message_to_screen(window, f"Food: {raw_food_count}", white, 0, 20)
        Functions.message_to_screen(window, f"Wood: {wood_count}", white, 0, 40)
        # Collision check for the player
        Functions.movement_controller_and_collision_check(player, player.rect, tree.rect) # Called here so it can use the returned rect value
        clock.tick(fps)
        pygame.display.update()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()