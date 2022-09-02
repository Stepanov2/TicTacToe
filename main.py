import numpy as np  # Cheats enabled=)
import globals
import inputprocessing
import gamerender
import gamelogic

# ========Querying user about what sort of game he/she wants=======

# request grid_size
print('Привет!\n Добро пожаловать в крестики нолики на "произвольном" поле (в 3D; на льду)')
_playerinput = input('Какого размера сделаем поле (от 3 до 10)? ')
while not inputprocessing.is_a_valid_int(_playerinput, lambda x: 3 <= x <= 10):
    _playerinput = input('Непонятненько! Какого размера сделаем поле (от 3 до 10)? ')
globals.grid_size = int(_playerinput)

# request in_line unless user prefers vanilla tic tac toe========
if globals.grid_size != 3:
    _playerinput = input(f'Отлично! Сколько нужно выстроить в линию, чтобы выиграть (от 3 до {globals.grid_size})? ')
    while not inputprocessing.is_a_valid_int(_playerinput, lambda x: 3 <= x <= globals.grid_size):
        _playerinput = input(f'Непонятненько! Ещё раз. Число от 3 до {globals.grid_size}? ')
globals.in_line = int(_playerinput)


# ===========Main loop============

while True:
    # initialize new game
    gamelogic.initialize_playfield()
    globals.current_player = 1
    gamerender.init_playfield()

    # ============Game is in progress loop=================

    while not gamelogic.check_win_condition() and 0 in globals.playfield:
        gamerender.print_playfield()
        _playerinput = input(f'Ходят {globals.whose_turn[globals.current_player]} ')

        while True:  # Checking that input is correct. Re-querying until it is.
            if not inputprocessing.is_a_valid_int(_playerinput, lambda x: 1 <= x <= globals.grid_size ** 2):
                gamerender.print_playfield()
                _playerinput = input(f'Ваш ход - инвалид. Введите целое число от 1 до {globals.grid_size ** 2} ')
                continue
            if not gamelogic.check_move_validity(int(_playerinput)):
                gamerender.print_playfield()
                _playerinput = input(f'Ваш ход - инвалид, ибо эта клетка уже занята! ')
                continue
            break

        gamerender.update_playfield(int(_playerinput))   # Updating game with (now validated) move
        globals.current_player *= -1                     # And swapping current player

    #======This game has just ended===========

    gamerender.print_playfield()
    if gamelogic.check_win_condition():
        print(f'Ура, победили {globals.whose_turn[gamelogic.check_win_condition()]}!')
    else:
        print('Ничья!')

    #=====Play again?=====
    _playerinput=input('Сыграем ещё раз? ')
    while inputprocessing.yes_or_no(_playerinput) is None:
        _playerinput = input('Таки да, или таки нет? ')
    if not inputprocessing.yes_or_no(_playerinput):
        print('See you later, alligator! ')
        quit(0)