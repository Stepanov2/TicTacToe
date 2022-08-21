"""functions to validate user input"""
import re
def yes_or_no(inputstring):
    """This tries to convert user input (string) to bool or returns None otherwise"""
    if not isinstance(inputstring, str): return None
    # leave only letters, digits and inner spaces
    inputstring = re.sub('[^ \w]', '', inputstring.strip().lower())
    yeslist = ('da', 'yes', 'yep', 'true', 'likely', 'да',
               'ага', 'пожалуй', 'давай', 'угу', 'вероятно')
    nolist = ('net', 'no', 'nope', 'false', 'unlikely', 'нет',
              'неа', 'да нет же', 'фигушки', 'маловероятно')
    if inputstring in yeslist:
        return True
    if inputstring in nolist:
        return False
    return None
def is_a_vaild_int(inputstring, condition=range(1,10)):
    """This checks that input is an int and in range [1..9]
    Specify different generator function to use this code elsewhere"""
    if not isinstance(inputstring, str): return Flase
    try:
        integer = int(inputstring)
    except ValueError:
        return False
    return integer in condition
