import numpy as np #Cheats enabled=)
import globals
import inputprocessing
import gamerender
import gamelogic








gamelogic.initialize_playfield()


while not gamelogic.check_win_condition():
    gamerender.return_playfield()
    playerinput = input(f'Ходят {globals.whose_turn[globals.currentplayer]} ')
    while True:
        if not inputprocessing.is_a_valid_int(playerinput, lambda x: 0 <= x <= globals.grid_size ** 2):
            gamerender.return_playfield()
            playerinput = input(f'Ваш ход - инвалид. Введите целое число от 1 до {globals.grid_size ** 2} ')
            continue
        if not gamelogic.check_move_validity(int(playerinput)):
            gamerender.return_playfield()
            playerinput = input(f'Ваш ход - инвалид, ибо эта клетка уже занята! ')
            continue
        break
gamerender.return_playfield()
print(f'Ура, победили {globals.whose_turn[-globals.currentplayer]}')

