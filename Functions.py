import time
from Classes import Objects
from pygame import font

def cooldown(times):
    time.sleep(times)


def draw_grid(surface, colour, size, no_of_squares, max_squares_in_row, starting_x, starting_y):

    rect_list = [Objects(HP=1, x=starting_x, y=starting_y) for _i in range(no_of_squares)]

    for i, rect in enumerate(rect_list):
        row, col = divmod(i, max_squares_in_row)
        rect.x_pos = col * size + starting_x
        rect.y_pos = row * size + starting_y
    
    
    for x in range(len(rect_list)):
        rect_list[x].draw(surface, colour, size_x=size, size_y=size, outline_only=True)

def draw_text(surface, size, text, colour, coords: tuple):
    font.init()
    lovebytes = font.Font("fonts/lovebytes.ttf", size)
    surface.blit(lovebytes.render(text, True, colour), coords)

def collision_check(rect1, rect2):
    if rect1.colliderect(rect2):
        return True
    return False