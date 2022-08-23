"""Functions related to printing stuff"""
import globals
import numpy as np  # Cheats enabled=)
from gamelogic import choice_to_index

_empty_playfield = []
_output = []
_cell_width=9
_cell_height=3
_c={  # Don't need most of those but whatever=)
'TLcorner': '┌',
'TRcorner': '┐',
'BLcorner': '└',
'BRcorner': '┘',
'cross':    '┿',
'Linters':  '├',
'Rinters':  '┤',
'Tinters':  '┬',
'Binters':  '┴',
'Hdash':    '─',
'Vdash':    '│'
}
_cross = (
    '   \\ /   ',
    '    ╳    ',
    '   / \\   '
    )
_noll = (
    '  ╭───╮  ',
    '  │   │  ',
    '  ╰───╯  '
    )
_none = ' ' * _cell_width


def _clearscreen():
    """Kinda. Sorta. Since os.system('cls') didn't work for me"""
    print('\n' * 40)


def _make_cell(number):
    """Envelop number with correct number of spaces"""
    return (_none, '    ' + str(number) + '   ' if number // 10 else '    ' + str(number) + '    ', _none)


def print_playfield():
    """Prints _output"""
    global _output
    _clearscreen()
    for i in range(len(_output)): print(_output[i])


def init_playfield():
    """Generate empty playfield graphic. i,j - index of element, y - index of line"""
    global _output
    global _empty_playfield

    # Do not run generation again, if it was already done in previous game
    if len(_empty_playfield):
        _output = _empty_playfield.copy()
        return

    _output=[]
    print_in_this_cell=()

    # Firstly, filling _output with correct number of empty strings
    for a in range(globals.grid_size * (_cell_height+1)-1):
        _output.append('')

    for i in range(globals.grid_size):
        for j in range(globals.grid_size):  # For each item in each row

            print_in_this_cell = _make_cell(i * globals.grid_size + j + 1)

            for y in range(_cell_height):
                # Appending cell content and vertical gridline unless it is last column
                _output[y + i * (_cell_height + 1)] += print_in_this_cell[y] + \
                                                       _c['Vdash'] * int(j != globals.grid_size - 1)
                # Appending horizontal gridline unless it is last row
            if i < globals.grid_size - 1:
                _output[_cell_height + i * (_cell_height + 1)] += _c['Hdash'] * _cell_width + \
                                                                  _c['cross'] * int(j != globals.grid_size - 1)

    _empty_playfield = _output.copy() # saving for later
    return


def update_playfield(move):
    """Replaces relevant part of _output with apropiate graphic when player makes a move"""
    global _output
    i, j = choice_to_index(move) #
    print_in_this_cell = ()

    if globals.playfield[i, j] == 1:  # What to print?
        print_in_this_cell = _cross
    elif globals.playfield[i, j] == -1:
        print_in_this_cell = _noll

    for line in range(0, _cell_height):
        fltmi = i * (_cell_height + 1)  # fltmi for first_line_to_modify_index
        _output[fltmi + line] = _output[fltmi + line][0:j * (_cell_width+1)] + \
                                print_in_this_cell[line] + \
                                _output[fltmi + line][(j + 1) * (_cell_width+1) - 1:]
