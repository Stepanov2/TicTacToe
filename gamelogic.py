"""Variables and functions to run the game
1 means cross
-1 means noll
0 means nothing"""
import globals
import numpy as np #Cheats enabled=)
def initialize_playfield():
    """Filling playfield with a matrix of zeroes"""
    globals.playfield = np.zeros((globals.grid_size, globals.grid_size), dtype=np.int16)
    return

def choice_to_index(choice):
    """Converts player's move to tuple, containing index of row and column"""

    choice -= 1
    return (choice // globals.grid_size, choice % globals.grid_size)

def check_win_condition(): #TODO let this get different playfield as an arg
    """Determines if the game was globals.in_line after this move.
    Returns 1 for crosses, -1 for nolls, False if no winner"""


    max_offset = globals.grid_size - globals.in_line
    
    #checking rows and columns
    for offset in range(max_offset + 1):

        for i in range(globals.grid_size):

            if abs(sum(globals.playfield[i, offset:globals.in_line + offset])) == globals.in_line:
                return globals.playfield[i, offset]
            if abs(sum(globals.playfield[offset:globals.in_line + offset, i])) == globals.in_line:
                return globals.playfield[offset, i]

    #checking diagonals
    #turning playfield into 1D array
    
    diagonals=globals.playfield.reshape(globals.grid_size ** 2)
    rotated_diagonals=np.rot90(globals.playfield).reshape(globals.grid_size ** 2)
    
    #for example, for 5x5 playfield and in_line=4 checking for elements
    #   0,6,12,18   1, 7, 13, 19   5, 11, 17, 23   6, 12, 18, 24
    #in both original and rotated playfield
    for offset_y in range(max_offset + 1):
        for offset_x in range(max_offset + 1):
            if abs(sum(diagonals[
                                offset_y * globals.grid_size + offset_x:
                                (globals.grid_size + 1) * (globals.in_line - 1 + offset_x) + offset_y + 1:
                                globals.grid_size + 1
                                ])) == globals.in_line:
                return diagonals[offset_y * globals.grid_size + offset_x]
            if abs(sum(rotated_diagonals[
                                offset_y * globals.grid_size + offset_x:
                                (globals.grid_size + 1) * (globals.in_line - 1 + offset_x) + offset_y + 1:
                                globals.grid_size + 1
                                ])) == globals.in_line:
                return rotated_diagonals[offset_y * globals.grid_size + offset_x]


    return False

def check_move_validity(move):
    """If attempted move was valid, advance the game"""
    move = choice_to_index(move)
    if globals.playfield[move] == 0:
        globals.playfield[move] = globals.current_player
        globals.current_player *= -1
        return True
    else:
        return False
