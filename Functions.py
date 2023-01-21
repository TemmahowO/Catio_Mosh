import pygame
from pygame.locals import *
import os

def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")



# Renders text to the screen
def message_to_screen(surface, msg, colour, pos_x, pos_y):
    font = pygame.font.SysFont(None, 25)
    screen_text = font.render(msg, True, colour)
    surface.blit(screen_text, [pos_x, pos_y])

# Takes care of player movement and collision
def movement_controller_and_collision_check(class_name, rect_one, rect_two):
    collision_true = pygame.Rect.colliderect(rect_one, rect_two)

    keys = pygame.key.get_pressed()
    if collision_true:
        class_name.x_pos -= class_name.x_speed
        class_name.x_speed = 0
    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        class_name.x_speed = 1
    elif keys[pygame.K_LEFT] or keys[pygame.K_a]:
         class_name.x_speed = -1
    else:
        class_name.x_speed = 0

    if collision_true:
        class_name.y_pos -= class_name.y_speed
        class_name.y_speed = 0
    if keys[pygame.K_UP] or keys[pygame.K_w]:
        class_name.y_speed = -1
    elif keys[pygame.K_DOWN] or keys[pygame.K_s]:
        class_name.y_speed = 1
    else: 
        class_name.y_speed = 0

    # Actually moves the player.
    class_name.x_pos += class_name.x_speed
    class_name.y_pos += class_name.y_speed

def keybinds(class_name, saturation, food):
    for event in pygame.event.get():
        pass
        