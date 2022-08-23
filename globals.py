import numpy as np  # Cheats enabled=)

whose_turn=('что-то сломалось!', 'крестики', 'нолики')  # whose_turn[1]='крестики' whose_turn[-1]='нолики' =))
grid_size = 3  # play on {grid_size} by {grid_size} playfield
in_line = 3  # match {in_line} in row to win
playfield = np.zeros((grid_size, grid_size), dtype=np.int8)
current_player = 1  # 1 means cross, -1 means noll
