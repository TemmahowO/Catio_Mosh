import pygame
from pygame.locals import Rect
from random import randint



# class Player:
#     def __init__(self, speed):
#         self.player_pos = Vector2d.Vector(randint(0, 500), randint(0, 500))
#         self.speed = speed

#         self.hitbox_rect = None
#         self.rect = None
#         self.x_speed = None
#         self.y_speed = None

#     def draw(self, surface, colour, size):
#         self.rect = Rect((self.player_pos.x, self.player_pos.y, size, size))
#         pygame.draw.rect(surface, colour, self.rect)

#         return self.rect

#     def draw_hitbox(self, surface, colour, player_size):
#         self.hitbox_rect = Rect(self.player_pos.x - player_size / 4, self.player_pos.y - player_size / 4, player_size + 10, player_size + 10)
#         pygame.draw.rect(surface, colour, self.hitbox_rect, 1)

#         return self.hitbox_rect

#     def update(self, event):
#         pass
#         # add in the code to switch between different sprites.

#     def player_controller(self, rect: list, collision=False):
#         keys = pygame.key.get_pressed()

#         if collision:
#             collision_true = Rect.colliderect(rect[0], rect[1])

#             if not collision_true:
#                 # Left and Right movement
#                 if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
#                     self.x_speed = self.speed
#                 elif keys[pygame.K_LEFT] or keys[pygame.K_a]:
#                     self.x_speed = -self.speed
#                 else:
#                     self.x_speed = 0

#                 # Up and Down movement
#                 if keys[pygame.K_UP] or keys[pygame.K_w]:
#                     self.y_speed = -self.speed
#                 elif keys[pygame.K_DOWN] or keys[pygame.K_s]:
#                     self.y_speed = self.speed
#                 else:
#                     self.y_speed = 0

#             if collision_true:
#                 self.player_pos.y -= self.y_speed
#                 self.y_speed = 0

#                 self.player_pos.x -= self.x_speed
#                 self.x_speed = 0

#         else:
#             # Left and Right movement
#             if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
#                 self.x_speed = self.speed
#             elif keys[pygame.K_LEFT] or keys[pygame.K_a]:
#                 self.x_speed = -self.speed
#             else:
#                 self.x_speed = 0

#             # Up and Down movement
#             if keys[pygame.K_UP] or keys[pygame.K_w]:
#                 self.y_speed = -self.speed
#             elif keys[pygame.K_DOWN] or keys[pygame.K_s]:
#                 self.y_speed = self.speed
#             else:
#                 self.y_speed = 0

#         self.player_pos.x += self.x_speed
#         self.player_pos.y += self.y_speed


# class Objects:
#     def __init__(self, durability=20, saturation=0):
#         self.object_pos = Vector2d.Vector(0, 0)
#         self.rect = None
#         self.size = 10

#     def draw(self, surface, colour, size=10, draw_outline=False):
#         self.rect = Rect((self.object_pos.x, self.object_pos.y, size, size))

#         if draw_outline:
#             pygame.draw.rect(surface, colour, self.rect, 1)
#         else:
#             pygame.draw.rect(surface, colour, self.rect)

#         return self.rect

pygame.init()

class Objects:
    def __init__(self, HP, x=0, y=0):
        self.exists = True
        self.x_pos = x
        self.y_pos = y
        self.hit_points = HP
        self.check_for_input = True
        
        
    def draw(self, surface, colour, size_x=20, size_y=20, outline_only=False):
        draw_rect = Rect((self.x_pos, self.y_pos, size_x, size_y))

        if self.exists and not outline_only:
            pygame.draw.rect(surface, colour, draw_rect)
        elif self.exists and outline_only:
            pygame.draw.rect(surface, colour, draw_rect, 1)

        return draw_rect

class Player(Objects):
    def movement(self, speed):
        keys = pygame.key.get_pressed()
        x_speed = 0
        y_speed = 0

        if self.check_for_input:
            # Left and Right movement
            if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
                x_speed = speed
            elif keys[pygame.K_LEFT] or keys[pygame.K_a]:
                x_speed = -speed
            else:
                x_speed = 0

            # Up and Down movement
            if keys[pygame.K_UP] or keys[pygame.K_w]:
                y_speed = -speed
            elif keys[pygame.K_DOWN] or keys[pygame.K_s]:
                y_speed = speed
            else:
                y_speed = 0
            
            self.x_pos += x_speed
            self.y_pos += y_speed