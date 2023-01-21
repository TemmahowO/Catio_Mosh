import pygame
from pygame.locals import Rect
from random import randint


class Player:
    def __init__(self, size):
        self.x_pos = randint(0, 500)
        self.y_pos = randint(0, 500)
        self.hunger = 50
        self.health = 100
        self.size = size
        self.rect = Rect((self.x_pos, self.y_pos, size, size))

    def health_system(self, is_eating, is_dead):
        if is_eating:
            self.hunger += 5
        else:
            self.hunger -= .1
            round(self.hunger, 2)
            if self.hunger <= 0:
                self.health -= .1
                if self.health <= 0:
                    is_dead = True
                    return is_dead

    def draw(self, window, colour, size):
        self.draw_x = self.x_pos
        self.draw_y = self.y_pos
        self.rect = Rect((self.x_pos, self.y_pos, size, size))
        
        pygame.draw.rect(window, colour, self.rect)
        return self.rect

    def draw_hitbox(self, window, colour, player_size):
        self.hitbox_rect = Rect(self.x_pos - player_size /2, self.y_pos - player_size /2, 20, 20) # Draws the hitbox at the center of the player.
        pygame.draw.rect(window, colour, self.hitbox_rect)
        return self.hitbox_rect

class Object:
    def __init__(self, durability, saturation, size):
        self.x_pos = randint(0, 500)
        self.y_pos = randint(0, 500)
        self.durability = durability
        self.size = size
        self.rect = Rect((self.x_pos, self.y_pos, size, size))
        self.saturation = saturation

    def draw(self, window, colour, size):
        self.draw_x = self.x_pos
        self.draw_y = self.y_pos
        self.rect = Rect((self.x_pos, self.y_pos, size, size))
        
        pygame.draw.rect(window, colour, self.rect)
        return self.rect

    def randomize_coords(self, window, colour, size):
        self.x_pos = randint(0, 500)
        self.y_pos = randint(0, 500)
        self.draw(window, colour, size)

