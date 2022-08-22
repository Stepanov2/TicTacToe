"""Functions related to printing stuff"""
import globals
import numpy as np #Cheats enabled=)

def print_playfield():

    charset = ('O', '.', 'X')
    for i in range(globals.grid_size):
        for j in range(globals.grid_size):
            print(charset[globals.playfield[i][j] + 1] + ' ', end='')
        print('')

    return