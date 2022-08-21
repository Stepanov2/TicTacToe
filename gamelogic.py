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
            grid_line.append(0) #aaaa
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
    #checking rows and columns
    for offset in range(max_offset + 1):

        for i in range(in_line):
            row_sum, col_sum = won, won

            for j in range(in_line):
                print(playfield[i][j+offset])
                row_sum-=playfield[i][j+offset]
                col_sum-=playfield[j+offset][i]
            if not row_sum or not col_sum:
                return True




    return False
initialize_playfield()
print(playfield)

print(check_win_condition(1))