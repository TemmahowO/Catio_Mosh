import pygame
from pygame.locals import Rect
from random import randint
from Maths import Vector2d

class Player:
    def __init__(self):
        self.player_pos = Vector2d.Vector(randint(0, 500), randint(0, 500))
        self.pixels_traveled = 0

    def draw(self, surface, colour, size):
        self.rect = Rect((self.player_pos.x, self.player_pos.y, size, size))
        pygame.draw.rect(surface, colour, self.rect)
    
    def draw_hitbox(self, surface, colour, player_size):
        self.hitbox_rect = Rect(self.x_pos - player_size /2, self.y_pos - player_size /2, 20, 20)
        pygame.draw.rect(surface, colour, self.hitbox_rect, 1)

    def update(self, event):
      pass
      # add in the code to switch between different sprites.

    def player_controller(self, debug_mode=False, debug_mode_X_Y=False, debug_mode_player_pos=False):
        keys = pygame.key.get_pressed()
        # Left and Right movement
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.x_speed = 5
        elif keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.x_speed = -5
        else:
            self.x_speed = 0
         
        # Up and Down movement
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            self.y_speed = -5
        elif keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.y_speed = 5
        else:
            self.y_speed = 0

        self.player_pos.x += self.x_speed
        self.player_pos.y += self.y_speed
    
        # Figure out how to make this more readable.
        # Maybe make a debug function.
        if debug_mode:
            if debug_mode_X_Y:
                print("Y_speed", self.y_speed)
                print("X_speed", self.x_speed)
            if debug_mode_player_pos:
                print("Player X Postion", self.player_pos.x)
                print("Player Y Position", self.player_pos.y)
