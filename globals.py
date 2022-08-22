import numpy as np #Cheats enabled=)
whose_turn=('что-то сломалось!', 'крестики', 'нолики') # whose_turn[1]='крестики' whose_turn[-1]='нолики' =))
username=''
grid_size = 3 #play on {grid_size} by {grid_size} playfield
in_line = 3 #match {in_line} in row to win1
playfield = np.zeros((grid_size, grid_size),dtype=np.int16)

current_player = 1
