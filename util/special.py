"""
Special functions.
"""


from util import validate as val


def Wait(p_question: str):
    """
    Waits for input from the user, usually used before closing a console program.

    Keyword arguments:
    p_question -- question posed to the user
    """
    input(p_question)
    return


def DrawLine(p_length: int, p_character: str):
    """
    Draws a line made of any character, with custom length.

    Keyword arguments:
    p_length -- length of the line
    p_character -- character of the line
    """
    print(p_character * p_length)
    return


def MenuWithBrackets(p_question: str):
    """
    Detects the characters between brackets in the p_question and validates
    the character that the user entered.
    Use the brackets in a similar way: "[S]tart match, [e]xit".
    You can't have two of the same characters in brackets.

    Keyword arguments:
    p_question -- question posed to the user    
    """
    choices = [];

    for c in range(0,len(p_question)):
        if (p_question[c] == '[' and p_question[c+2] == ']'):
            choices.append((p_question[c+1]).lower())

    while True:
        character = (val.Char(p_question)).lower()
        
        if (character not in choices):
            print("***Enter a character between brackets you dangus.")
        else:
            return character


def RotateList(p_l: list, p_n: int):
    """
    Rotates a list of n positions

    Keyword arguments:
    p_l -- a list
    p_n -- number of rotation
    """
    return p_l[p_n:] + p_l[:p_n]