"""Functions related to printing stuff"""
from globals import *

def print_playfield():
    global playfield
    global grid_size
    charset = ('○', '▯', 'X')
    for i in range(grid_size):
        for j in range(grid_size):
            print(charset[playfield[i][j] + 1])

    return