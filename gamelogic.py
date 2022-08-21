"""Variables and functions to run the game
1 means cross
-1 means null
0 means nothing"""
username=''
playfield = []
grid_size = 3 #play on {grid_size} by {grid_size} playfield
in_line = 3 #match {in_line} in row to win
def initialize_playfield():
    """Filling playfield with a matrix of zeroes"""
    global playfield
    global grid_size
    playfield = []
    for i in range(grid_size):
        grid_line=[]
        for j in range(grid_size):
            grid_line.append([0])
        playfield.append(grid_line)
    return

def choice_to_index(choice):
    """Converts player's move to tuple, containing index of row and column"""
    global grid_size
    choice -= 1
    return (choice // grid_size, choice % grid_size)

def check_win_condition(one_or_minus_one):
    """Determines if the game was one after this move"""
    global playfield
    global grid_size
    global in_line
    won = one_or_minus_one * in_line
    max_offset = grid_size - in_line
    #checking rows
    for i in range(0, grid_size):
        for j in range(0, max_offset + 1):
            print(playfield[i][j:j + in_line])
            if sum(playfield[i][j:j + in_line]) == won:
                #ПОЧЕМУ ЭТО НЕ РАБОТАЕТ?11
                return True

    return
initialize_playfield()
#print(playfield[0][0:3])

check_win_condition(1)