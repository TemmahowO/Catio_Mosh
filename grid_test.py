import pygame
from pygame.locals import Rect

white = [255, 255, 255]
black = [0, 0, 0]


# def drawGrid(SCREEN, window_width, window_height, COLOUR, rect, rect_x, rect_y):
#     blockSize = 50 #Set the size of the grid block
#     for x in range(0, window_width // blockSize):
#         for y in range(0, window_height // blockSize):
#             grid_rect = pygame.Rect(x, y, blockSize, blockSize)
#             pygame.draw.rect(SCREEN, COLOUR, grid_rect, 1)
            
#         if pygame.Rect.colliderect(grid_rect, rect):
#             rect_y = y + blockSize / 2
#             rect_x = x + blockSize / 2
#             print("hello")

#             return rect_y, rect_x


# Rect list defined 
def Inventory(window, colour,  screen_width, screen_height, rect_list2, size, offset=100):
    rect_list = [Rect(screen_width /2 - offset, screen_height /2, size, size), Rect(screen_width /2 - offset + size, screen_height /2, size, size), Rect(screen_width /2 - offset + size *2, screen_height /2, size, size), Rect(screen_width /2 - offset + size *3, screen_height /2, size, size)]
    for i in range(4):
        pygame.draw.rect(window, colour, rect_list[i], 1)
    return rect_list, size
# window_width = 500
# window_height = 500
# game_on = True

# window = pygame.display.set_mode((window_width, window_height))
# pygame.display.set_caption("Moshi Game")

# while game_on == True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             game_on = False
#     window.fill(white)
#     Inventory(window, black, window_width, window_height, 50)
#     pygame.display.update()


