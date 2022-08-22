import numpy as np #Cheats enabled=)
import globals
import inputprocessing
import gamerender
import gamelogic








gamelogic.initialize_playfield()

globals.playfield[2] = [-1,0,1]
globals.playfield[0][1]=1
globals.playfield[1][1]=1
globals.playfield[2][1]=1


gamerender.print_playfield()
print(gamelogic.check_win_condition(1))


print(globals.playfield[0][0:3])
print(globals.playfield[1][0:3])
print(globals.playfield[2][0:3])
print()
print(globals.playfield[0:3][0])
print(globals.playfield[0:3][1])
print(globals.playfield[0:3][2])

print(inputprocessing.is_a_vaild_int('3'), range(0,7))
print(inputprocessing.is_a_vaild_int('15'), range(0,7))
print(inputprocessing.is_a_vaild_int('-2'), range(0,7))
