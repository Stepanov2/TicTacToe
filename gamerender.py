"""Functions related to printing stuff"""
import globals
import numpy as np #Cheats enabled=)




def clearscreen():
    """Kinda. Sorta. os.system('cls') didn't work for me"""
    print('\n' * 40)

_cell_width=9
_cell_height=3
c={
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
'Vdash':    '┆'
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

def make_cell(number):
    """envelop number with correct number of spaces"""
    return (_none, '    ' + str(number) + '   ' if number // 10 else '    ' + str(number) + '    ', _none)
def print_playfield():
    """Main rendering function. i,j - index of element, y - index of line"""
    output = []
    print_in_this_cell=()
    for a in range(globals.grid_size * (_cell_height+1)-1):
        output.append('') #Filling output with correct number of empty strings
    for i in range(globals.grid_size):
        for j in range(globals.grid_size):#for each item in each row
            #figure out what to print in this cell
            if globals.playfield[i, j] == 1:
                print_in_this_cell = _cross
            elif globals.playfield[i, j] == -1:
                print_in_this_cell = _noll
            else:
                print_in_this_cell = make_cell(i * globals.grid_size + j + 1)
            for y in range(_cell_height):
                #appending cell content
                output[y + i * (_cell_height + 1)] += print_in_this_cell[y] + c['Vdash'] * int(j != globals.grid_size - 1)
                #appending horizontal gridline unless last row
            if i < globals.grid_size - 1:
                output[_cell_height + i * (_cell_height + 1)] += c['Hdash'] * _cell_width + c['cross'] * int(j != globals.grid_size - 1)

    #and, finally,  printing
    for i in range(len(output)): print(output[i])


    return