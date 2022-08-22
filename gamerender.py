"""Functions related to printing stuff"""
import globals
import numpy as np #Cheats enabled=)



def clearscreen():
    print('\n' * 40)

#TODO: подумать, как это всё таки перепилить с декораторами
""" 
def _charsetpicker(i,j):
    charset = ('O', '.', 'X')
    return charset(globals.playfield[i, j] + 1)




def _playfield_prototype(whatvalue):
    \"""Turns into return_playfield and return_choices via decorators""\"

    for i in range(globals.grid_size):
        for j in range(globals.grid_size):
            print(whatvalue(i, j) + ' ', end='')
        print('')

    return
"""
#return_playfield = _playfield_prototype(_charsetpicker)

def return_playfield():
    """Turns into return_playfield and return_choices via decorators"""

    def whatvalue(i, j):
        charset = ('O', '.', 'X')
        return charset[globals.playfield[i, j] + 1]

    for i in range(globals.grid_size):
        for j in range(globals.grid_size):
            print(' ' + whatvalue(i, j) + ' ', end='')
        print('')

    return

def return_grid():
    """Turns into return_playfield and return_choices via decorators"""

    def whatvalue(i, j):
        return i * globals.grid_size + j + 1

    for i in range(globals.grid_size):
        for j in range(globals.grid_size):
            print('%2d' % (whatvalue(i, j)) + ' ', end='')
        print('')

    return