import pygame
import sys
from pygame.locals import Rect
from grid_test import Inventory
import time

def inventory_UI():
    handled = False
    handled2 = False
    white = [255, 255, 255]
    green = [0, 255, 0]
    blue = [0, 0, 255]
    gray = [25, 25, 25]
    window_width = 400
    window_height = 400
    window = pygame.display.set_mode((window_height, window_width))
    pygame.display.set_caption("UI&Inventory Test")
    square_x = 200
    square_y = 200
    square_size = 20
    held = False
    already_pressed = False
    in_inventory_slot = False
    inventory_visable = True
    rect_list = []
    clock = pygame.time.Clock()
    mouse_x_pos = pygame.mouse.get_pos()[0] - square_size /2
    mouse_y_pos = pygame.mouse.get_pos()[1] - square_size /2
    square_rect_not_held = Rect(square_x, square_y, 20, 20)
    square_rect_held = Rect(mouse_x_pos - 999, mouse_y_pos - 999, 20, 20)

    while True:
        mouse_x_pos = pygame.mouse.get_pos()[0] - square_size /2
        mouse_y_pos = pygame.mouse.get_pos()[1] - square_size /2
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
               sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed()[0] and square_rect_not_held.collidepoint(pygame.mouse.get_pos()) and not handled:
                    #square_rect_held = Rect(mouse_x_pos - 20, mouse_y_pos - 20, 20, 20)
                    held = True
                    square_x = mouse_x_pos
                    square_y = mouse_y_pos
                if pygame.mouse.get_pressed()[0] and square_rect_held.collidepoint(pygame.mouse.get_pos()) and not handled2:
                    held = False
                    square_x = mouse_x_pos
                    square_y = mouse_y_pos
                
            if event.type == pygame.KEYDOWN and event.key == pygame.K_e:
                    if already_pressed:
                        already_pressed = False
                        inventory_visable = True

                    elif not already_pressed:
                        inventory_visable = False
                        already_pressed = True

        square_rect_not_held = Rect(square_x, square_y, 20, 20)
        square_rect_held = Rect(mouse_x_pos, mouse_y_pos, 20, 20)

        window.fill(white) 
       
        if inventory_visable:
            rect_list, size = Inventory(window, gray, window_width, window_height, rect_list, size=50, offset=100)

            if not held:
                square_rect_held = Rect(mouse_x_pos - 999, mouse_y_pos - 999, 20, 20)
                pygame.draw.rect(window, blue, square_rect_not_held)
            elif held:
                square_rect_held = Rect(mouse_x_pos, mouse_y_pos, 20, 20)
                pygame.draw.rect(window, green, square_rect_held)

            # To be fair, I am not entirely sure why or how this works and I am too tired to understand this.
            if Rect.colliderect(rect_list[0], square_rect_not_held):
                square_x = rect_list[0][0] - size /2 + 40
                square_y = rect_list[0][1] - size /2 + 40
                in_inventory_slot = True
            elif Rect.colliderect(rect_list[1], square_rect_not_held):
                square_x = rect_list[1][0] - size /2 + 40
                square_y = rect_list[1][1] - size /2 + 40
                in_inventory_slot = True
            elif Rect.colliderect(rect_list[2], square_rect_not_held):
                square_x = rect_list[2][0] - size /2 + 40
                square_y = rect_list[2][1] - size /2 + 40
                in_inventory_slot = True
            elif Rect.colliderect(rect_list[3], square_rect_not_held):
                square_x = rect_list[3][0] - size /2 + 40
                square_y = rect_list[3][1] - size /2 + 40
                in_inventory_slot = True
            else:
                in_inventory_slot = False


        handled = pygame.mouse.get_pressed()[0]
        clock.tick(30)
        pygame.display.update()


if __name__ == "__main__":
    pygame.init()
    inventory_UI()
