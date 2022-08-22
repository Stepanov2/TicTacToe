"""Variables and functions to run the game
1 means cross
-1 means null
0 means nothing"""
import globals
def initialize_playfield():
    """Filling playfield with a matrix of zeroes"""
    globals.playfield = []
    for i in range(globals.grid_size):
        grid_line=[]
        for j in range(globals.grid_size):
            grid_line.append(0)
        globals.playfield.append(grid_line)
    return

def choice_to_index(choice):
    """Converts player's move to tuple, containing index of row and column"""

    choice -= 1
    return (choice // globals.grid_size, choice % globals.grid_size)

def check_win_condition(one_or_minus_one):
    """Determines if the game was won after this move"""

    won = one_or_minus_one * globals.in_line

    max_offset = globals.grid_size - globals.in_line
    #checking rows and columns
    for offset in range(max_offset + 1):

        for i in range(globals.grid_size):

            if sum(globals.playfield[i][offset:globals.grid_size + offset]) == won: return True
            #print(sum(playfield[i][offset:grid_size + offset]))
            #print(sum(playfield[offset:grid_size + offset][i]))
            if sum(globals.playfield[offset:globals.grid_size + offset][i]) == won: return True







    return False


