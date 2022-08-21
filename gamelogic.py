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

        for i in range(grid_size):

            if sum(playfield[i][offset:grid_size + offset]) == won: return True
            print(sum(playfield[i][offset:grid_size + offset]))
            print(sum(playfield[offset:grid_size + offset][i]))
            if sum(playfield[offset:grid_size + offset][i]) == won: return True







    return False
initialize_playfield()

playfield[2] = [-1,0,1]
playfield[0][1]=1
playfield[1][1]=1
playfield[2][1]=1
print(playfield)
print(check_win_condition(1))