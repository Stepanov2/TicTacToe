import globals
import unittest
from gamelogic import check_win_condition
import numpy as np


class testWincrosses(unittest.TestCase):

    def test_wins(self):
       
        for globals.grid_size in range(3, 11):
            zeroed_matrix = np.zeros((globals.grid_size, globals.grid_size), dtype=np.int8)
            h_in_matrix = zeroed_matrix.copy()
            v_in_matrix = zeroed_matrix.copy()
            d1_in_matrix = zeroed_matrix.copy()
            d2_in_matrix = zeroed_matrix.copy()

            for globals.in_line in range(3, globals.grid_size+1):
                print(f'{globals.grid_size =} {globals.in_line =}')
                # testing lines
                for offset_y in range(globals.grid_size):
                    for offset_x in range(globals.grid_size - globals.in_line + 1):
                        h_in_matrix = zeroed_matrix.copy()
                        v_in_matrix = zeroed_matrix.copy()
                        for i in range(globals.in_line):
                            h_in_matrix[offset_y, offset_x + i] = 1
                            v_in_matrix[ offset_x + i, offset_y] = 1
                        print(h_in_matrix)
                        print(v_in_matrix)
                        globals.playfield = h_in_matrix.copy()
                        self.assertEqual(check_win_condition(), 1,
                                         msg=f'{globals.grid_size = }, {globals.in_line = }\n{globals.playfield}')
                        globals.playfield = np.negative(globals.playfield)
                        self.assertEqual(check_win_condition(), -1,
                                         msg=f'{globals.grid_size = }, {globals.in_line = }\n{globals.playfield}')
                        globals.playfield = v_in_matrix.copy()
                        self.assertEqual(check_win_condition(), 1,
                                         msg=f'{globals.grid_size = }, {globals.in_line = }\n{globals.playfield}')
                        globals.playfield = np.negative(globals.playfield)
                        self.assertEqual(check_win_condition(), -1,
                                         msg=f'{globals.grid_size = }, {globals.in_line = }\n{globals.playfield}')
                # testing diagonals
                max_offset = globals.grid_size - globals.in_line + 1

                for offset_y in range(max_offset):
                    for offset_x in range(max_offset):
                        d1_in_matrix = zeroed_matrix.copy()
                        d2_in_matrix = zeroed_matrix.copy()
                        for i in range(globals.in_line):

                            d1_in_matrix[offset_y+i, offset_x+i] = 1
                            d2_in_matrix[globals.grid_size-1-offset_y - i, offset_x+i] = 1
                        print(d1_in_matrix)
                        print(d2_in_matrix)
                        globals.playfield = d1_in_matrix.copy()
                        self.assertEqual(check_win_condition(), 1,
                                         msg=f'{globals.grid_size = }, {globals.in_line = }\n{globals.playfield}')
                        globals.playfield = np.negative(globals.playfield)
                        self.assertEqual(check_win_condition(), -1,
                                         msg=f'{globals.grid_size = }, {globals.in_line = }\n{globals.playfield}')
                        globals.playfield = d2_in_matrix.copy()
                        self.assertEqual(check_win_condition(), 1,
                                         msg=f'{globals.grid_size = }, {globals.in_line = }\n{globals.playfield}')
                        globals.playfield = np.negative(globals.playfield)
                        self.assertEqual(check_win_condition(), -1,
                                         msg=f'{globals.grid_size = }, {globals.in_line = }\n{globals.playfield}')



