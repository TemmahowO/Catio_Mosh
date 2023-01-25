import pygame
from pygame.locals import *
import sys
from Classes import * 
import Functions


def main():
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
    inventory_visable = False
    already_pressed = True
    raw_food_count = 0
    wood_count = 0

    handled = False
    handled2 = False
    square_x = 200
    square_y = 200
    square_size = 20
    held = False
    rect_list = []
    mouse_x_pos = pygame.mouse.get_pos()[0] - square_size /2
    mouse_y_pos = pygame.mouse.get_pos()[1] - square_size /2
    square_rect_not_held = Rect(square_x, square_y, 20, 20)
    square_rect_held = Rect(mouse_x_pos - 999, mouse_y_pos - 999, 20, 20)



    player = Player(10)
    tree = Object(5, 0, 20)
    food = Object(1, 10, 5)
    wood = Object(1, 0, 10)


    window = pygame.display.set_mode((window_width, window_height))
    pygame.display.set_caption("Moshi Game")

    while Game_on == True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Game_on = False
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_e:
                    if already_pressed:
                        already_pressed = False
                        inventory_visable = True

                    elif not already_pressed:
                        inventory_visable = False
                        already_pressed = True

                if pygame.mouse.get_pressed()[0] and square_rect_not_held.collidepoint(pygame.mouse.get_pos()) and not handled:
                    held = True
                    square_x = mouse_x_pos
                    square_y = mouse_y_pos
                if pygame.mouse.get_pressed()[0] and square_rect_held.collidepoint(pygame.mouse.get_pos()) and not handled2:
                    held = False
                    square_x = mouse_x_pos
                    square_y = mouse_y_pos            


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

        ## Collision detection ##
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

        window.fill(gray)

        ## Inventory system ##
        if inventory_visable:
            rect_list, size = Functions.Inventory(window, white, window_width, window_height, size=30, offset=100)
            
            if not held:
                square_rect_held = Rect(mouse_x_pos - 999, mouse_y_pos - 999, 20, 20)
                pygame.draw.rect(window, green, square_rect_not_held)
            elif held:
                square_rect_held = Rect(mouse_x_pos, mouse_y_pos, 20, 20)
                pygame.draw.rect(window, green, square_rect_held)

            # To be fair, I am not entirely sure why or how this works and I am too tired to understand this.
            if Rect.colliderect(rect_list[0], square_rect_not_held):
                square_x = rect_list[0][0] - size /2 + size - 10
                square_y = rect_list[0][1] - size /2 + size - 10
            elif Rect.colliderect(rect_list[1], square_rect_not_held):
                square_x = rect_list[1][0] - size /2 + size - 10
                square_y = rect_list[1][1] - size /2 + size - 10
            elif Rect.colliderect(rect_list[2], square_rect_not_held):
                square_x = rect_list[2][0] - size /2 + size - 10
                square_y = rect_list[2][1] - size /2 + size - 10
            elif Rect.colliderect(rect_list[3], square_rect_not_held):
                square_x = rect_list[3][0] - size /2 + size - 10
                square_y = rect_list[3][1] - size /2 + size - 10

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
    pygame.init()
    main()