"""
Validate what the user entered and handle exceptions.
"""


import time


CURSOR_UP_ONE = '\x1b[1A' # Moves the cursor up one line
ERASE_LINE = '\x1b[2K'

class bcolors:
    """
    A class that lets you use colors in the console.

    HEADER is purple.
    OKBLUE is dark blue.
    OKGREEN is green.
    WARNING is yellow.
    FAIL is red.
    ENDC is the normal color. You use this after using any color.
    BOLD is white.
    UNDERLINE underlines text.
    """
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


"""
INT validators.
"""
def Int(p_question: str):
    """
    Validates the Int that the user entered.

    Keyword arguments:
    p_question -- question posed to the user
    """
    while True:
        try:
            number = int(input(ERASE_LINE + p_question))
            return number
        except ValueError:
            print(CURSOR_UP_ONE + ERASE_LINE + bcolors.FAIL + "***Enter a number without decimals you dangus." + bcolors.ENDC, end="\r")
            time.sleep(3)



def PositiveInt(p_question: str):
    """
    Validates the positive Int that the user entered.
    0 isn't counted as a positive number.

    Keyword arguments:
    p_question -- question posed to the user
    """
    while True:
        number = Int(ERASE_LINE + p_question)
        if (number < 1):
            print(CURSOR_UP_ONE + ERASE_LINE + bcolors.FAIL + "***Enter a positive number you dangus." + bcolors.ENDC, end="\r")
            time.sleep(3)
        else:
            return number

def PositiveIntZeroIncluded(p_question: str):
    """
    Validates the positive Int that the user entered.
    0 is counted as a positive number.

    Keyword arguments:
    p_question -- question posed to the user
    """
    while True:
        number = Int(ERASE_LINE + p_question)
        if (number < 0):
            print(CURSOR_UP_ONE + ERASE_LINE + bcolors.FAIL + "***Enter a positive number you dangus." + bcolors.ENDC, end="\r")
            time.sleep(3)
        else:
            return number


def NegativeInt(p_question: str):
    """
    Validates the negative Int that the user entered.
    0 isn't counted as a negative number.

    Keyword arguments:
    p_question -- question posed to the user
    """
    while True:
        number = Int(ERASE_LINE + p_question)
        if (number > 1):
            print(CURSOR_UP_ONE + ERASE_LINE + bcolors.FAIL + "***Enter a negative number you dangus." + bcolors.ENDC, end="\r")
            time.sleep(3)
        else:
            return number


def NegativeIntZeroIncluded(p_question: str):
    """
    Validates the negative Int that the user entered.
    0 is counted as a negative number.

    Keyword arguments:
    p_question -- question posed to the user
    """
    while True:
        number = Int(ERASE_LINE + p_question)
        if (number > 0):
            print(CURSOR_UP_ONE + ERASE_LINE + bcolors.FAIL + "***Enter a negative number you dangus." + bcolors.ENDC, end="\r")
            time.sleep(3)
        else:
            return number


def IntWithMinimum(p_question: str, p_minimum: int):
    """
    Validates the Int that the user entered with a minimum imposed.

    Keyword arguments:
    p_question -- question posed to the user
    p_minimum -- the minimum number
    """
    while True:
        number = Int(ERASE_LINE + p_question)
        if (number < p_minimum):
            print(CURSOR_UP_ONE + ERASE_LINE + bcolors.FAIL + "***Enter a number above or equal to {} you dangus.".format(p_minimum) + bcolors.ENDC, end="\r")
            time.sleep(3)
        else:
            return number


def IntWithMaximum(p_question: str, p_maximum: int):
    """
    Validates the Int that the user entered with a maximum imposed.

    Keyword arguments:
    p_question -- question posed to the user
    p_maximum -- the maximum number
    """
    while True:
        number = Int(ERASE_LINE + p_question)
        if (number > p_maximum):
            print(CURSOR_UP_ONE + ERASE_LINE + bcolors.FAIL + "***Enter a number lower or equal to {} you dangus.".format(p_maximum) + bcolors.ENDC, end="\r")
            time.sleep(3)
        else:
            return number


def IntInsideInterval(p_question: str, p_minimum: int, p_maximum: int):
    """
    Validates the Int that the user entered with an interval imposed.

    Keyword arguments:
    p_question -- question posed to the user
    p_minimum -- the minimum number
    p_maximum -- the maximum number
    """
    while True:
        number = Int(ERASE_LINE + p_question)
        if (p_minimum > number or number > p_maximum):
            print(CURSOR_UP_ONE + ERASE_LINE + bcolors.FAIL + "***Enter a number between {} and {} you dangus.".format(p_minimum,p_maximum) + bcolors.ENDC, end="\r")
            time.sleep(3)
        else:
            return number


def RepresentsInt(p_s):
    """
    Returns True if the value is an int.
    Returns False if the value is not an int.

    Keyword arguments:
    p_s -- value we want to test
    """
    try: 
        int(p_s)
        return True
    except ValueError:
        return False


"""
FLOAT validators.
"""
def Float(p_question: str):
    """
    Validates the Float that the user entered.

    Keyword arguments:
    p_question -- question posed to the user
    """
    while True:
        try:
            number = float(input(ERASE_LINE + p_question))
            return number
        except ValueError:
            print(CURSOR_UP_ONE + ERASE_LINE + bcolors.FAIL + "***Enter a number you dangus." + bcolors.ENDC, end="\r")
            time.sleep(3)


def PositiveFloat(p_question: str):
    """
    Validates the positive Float that the user entered.

    Keyword arguments:
    p_question -- question posed to the user
    """
    while True:
        number = Float(ERASE_LINE + p_question)
        if (number < 1.0):
            print(CURSOR_UP_ONE + ERASE_LINE + bcolors.FAIL + "***Enter a positive number you dangus." + bcolors.ENDC, end="\r")
            time.sleep(3)
        else:
            return number


def Negativefloat(p_question: str):
    """
    Validates the negative Float that the user entered.

    Keyword arguments:
    p_question -- question posed to the user
    """
    while True:
        number = Float(ERASE_LINE + p_question)
        if (number > 0.0):
            print(CURSOR_UP_ONE + ERASE_LINE + bcolors.FAIL + "***Enter a negative number you dangus." + bcolors.ENDC, end="\r")
            time.sleep(3)
        else:
            return number


def FloatWithMinimum(p_question: str, p_minimum: float):
    """
    Validates the Float that the user entered with a minimum imposed.

    Keyword arguments:
    p_question -- question posed to the user
    p_minimum -- the minimum number
    """
    while True:
        number = Float(ERASE_LINE + p_question)
        if (number < p_minimum):
            print(CURSOR_UP_ONE + ERASE_LINE + bcolors.FAIL + "***Enter a number above or equal to {} you dangus.".format(p_minimum) + bcolors.ENDC, end="\r")
            time.sleep(3)
        else:
            return number


def FloatWithMaximum(p_question: str, p_maximum: float):
    """
    Validates the Float that the user entered with a maximum imposed.

    Keyword arguments:
    p_question -- question posed to the user
    p_maximum -- the maximum number
    """
    while True:
        number = Float(ERASE_LINE + p_question)
        if (number > p_maximum):
            print(CURSOR_UP_ONE + ERASE_LINE + bcolors.FAIL + "***Enter a number lower or equal to {} you dangus.".format(p_maximum) + bcolors.ENDC, end="\r")
            time.sleep(3)
        else:
            return number


def FloatInsideInterval(p_question: str, p_minimum: float, p_maximum: float):
    """
    Validates the Float that the user entered with an interval imposed.

    Keyword arguments:
    p_question -- question posed to the user
    p_minimum -- the minimum number
    p_maximum -- the maximum number
    """
    while True:
        number = Float(ERASE_LINE + p_question)
        if (p_minimum > number or number > p_maximum):
            print(CURSOR_UP_ONE + ERASE_LINE + bcolors.FAIL + "***Enter a number between {} and {} you dangus.".format(p_minimum,p_maximum) + bcolors.ENDC, end="\r")
            time.sleep(3)
        else:
            return number


"""
STRING validators.
"""
def String(p_question: str):
    """
    Validates the String that the user entered.

    Keyword arguments:
    p_question -- question posed to the user
    """
    while True:
        try:
            text = str(input(ERASE_LINE + p_question))
            return text
        except Exception:
            print(CURSOR_UP_ONE + ERASE_LINE + bcolors.FAIL + "***Enter normal characters you dangus." + bcolors.ENDC, end="\r")
            time.sleep(3)


def StringTrim(p_question: str):
    """
    Trims the validated String that the user entered.

    Keyword arguments:
    p_question -- question posed to the user
    """
    text = (String(p_question)).strip()
    return text


def Char(p_question: str):
    """
    Validates the Character that the user entered.

    Keyword arguments:
    p_question -- question posed to the user
    """
    while True:
        character = String(ERASE_LINE + p_question)
        if (len(character) == 0 or len(character) > 1):
            print(CURSOR_UP_ONE + ERASE_LINE + bcolors.FAIL + "***Enter one normal character you dangus." + bcolors.ENDC, end="\r")
            time.sleep(3)
        else:
            return character