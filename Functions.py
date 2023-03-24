import time
from Classes import Objects
import pygame


def debug_mode(*variables):
    var_number = 1
    for print_vars in variables:
        print(f"Variable {var_number}: {print_vars}")
        var_number += 1


def cooldown(times):
    time.sleep(times)


def draw_grid(surface, colour, size, no_of_squares, no_of_rows, squares_in_row,
              starting_x):
    no_of_squares_in_row = 0
    rect_list = [Objects() for _i in range(no_of_squares)]
    rect_list[0].object_pos.x = starting_x

    for i in range(1, len(rect_list)):
        rect_list[i].object_pos.x = starting_x + size * i
        no_of_squares_in_row += 1
        if no_of_squares_in_row >= squares_in_row:
            no_of_rows += 1
            rect_list[i].object_pos.x -= size * no_of_rows
            rect_list[i].object_pos.y += size * no_of_rows

    for x in range(len(rect_list)):
        rect_list[x].draw(surface, colour, size, True)

