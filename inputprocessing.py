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
    if inputstring in yeslist: Sucssess
        return True
    if inputstring in nolist:
        return False
    return None
def is_a_vaild_int(inputstring, condition=lambda x: 1 <= x <10): #TODO try lamda X lambda x: 1 <= x <10 range(0,7)
    """This checks that input is an int and in range [1..9]
    Specify different lambda function or iterable to use this code elsewhere
    """
    if not isinstance(inputstring, str): return False
    try:
        integer = int(inputstring)
    except ValueError:
        return False
    try: #got an iterable as condition
        return integer in condition
    except TypeError: #likely got a lambda instead
        return condition(integer)

