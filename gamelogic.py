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
    """Determines if the game was won after this move. Returns 1 for crosses, -1 for nolls, 0 if no winner"""

    won = globals.in_line

    max_offset = globals.grid_size - globals.in_line
    #checking rows and columns
    for offset in range(max_offset + 1):

        for i in range(globals.grid_size):

            if abs(sum(globals.playfield[i, offset:globals.in_line + offset])) == won:
                return globals.playfield[i, offset]
            if abs(sum(globals.playfield[offset:globals.in_line + offset, i])) == won:
                return globals.playfield[offset, i]

        #TODO diagonals!!

    return False

def check_move_validity(move):
    """Если клетка свободна двигаем игру вперёд"""
    move = choice_to_index(move)
    if globals.playfield[move] == 0:
        globals.playfield[move] = globals.currentplayer
        globals.currentplayer *= -1
        return True
    else:
        return False
