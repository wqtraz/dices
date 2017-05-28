"""
Validate what the user entered and handle exceptions.
"""

"""
INT validators.
"""

def Int(p_question:str):
    """
    Validates the Int that the user entered.

    Keyword arguments:
    p_question -- question posed to the user
    """
    while True:
        try:
            number = int(input(p_question))
            return number
        except ValueError:
            print("***Enter a number without decimals you dangus")


def PositiveInt(p_question:str):
    """
    Validates the positive Int that the user entered.

    Keyword arguments:
    p_question -- question posed to the user
    """
    while True:
        number = ValidateInt(p_question)
        if (number < 0):
            print("***Enter a positive number you dangus")
        else:
            return number


def NegativeInt(p_question:str):
    """
    Validates the negative Int that the user entered.

    Keyword arguments:
    p_question -- question posed to the user
    """
    while True:
        number = ValidateInt(p_question)
        if (number > 0):
            print("***Enter a negative number you dangus")
        else:
            return number


def IntWithMinimum(p_question:str, p_minimum:int):
    """
    Validates the Int that the user entered with a minimum imposed.

    Keyword arguments:
    p_question -- question posed to the user
    p_minimum -- the minimum number
    """
    while True:
        number = ValidateInt(p_question)
        if (number < p_minimum):
            print("***Enter a number above or equal to {} you dangus".format(p_minimum))
        else:
            return number


def IntWithMaximum(p_question:str, p_maximum:int):
    """
    Validates the Int that the user entered with a maximum imposed.

    Keyword arguments:
    p_question -- question posed to the user
    p_maximum -- the maximum number
    """
    while True:
        number = ValidateInt(p_question)
        if (number > p_maximum):
            print("***Enter a number lower or equal to {} you dangus".format(p_maximum))
        else:
            return number


def IntInsideInterval(p_question:str, p_minimum:int, p_maximum:int):
    """
    Validates the Int that the user entered with an interval imposed.

    Keyword arguments:
    p_question -- question posed to the user
    p_minimum -- the minimum number
    p_maximum -- the maximum number
    """
    while True:
        number = ValidateInt(p_question)
        if (p_minimum > number or number > p_maximum):
            print("***Enter a number between {} and {} you dangus".format(p_minimum,p_maximum))
        else:
            return number


"""
FLOAT validators.
"""

def Float(p_question:str):
    """
    Validates the Float that the user entered.

    Keyword arguments:
    p_question -- question posed to the user
    """
    while True:
        try:
            number = float(input(p_question))
            return number
        except ValueError:
            print("***Enter a number you dangus")


def PositiveFloat(p_question:str):
    """
    Validates the positive Float that the user entered.

    Keyword arguments:
    p_question -- question posed to the user
    """
    while True:
        number = ValidateFloat(p_question)
        if (number < 0.0):
            print("***Enter a positive number you dangus")
        else:
            return number


def Negativefloat(p_question:str):
    """
    Validates the negative Float that the user entered.

    Keyword arguments:
    p_question -- question posed to the user
    """
    while True:
        number = ValidateFloat(p_question)
        if (number > 0.0):
            print("***Enter a negative number you dangus")
        else:
            return number


def FloatWithMinimum(p_question:str, p_minimum:float):
    """
    Validates the Float that the user entered with a minimum imposed.

    Keyword arguments:
    p_question -- question posed to the user
    p_minimum -- the minimum number
    """
    while True:
        number = ValidateFloat(p_question)
        if (number < p_minimum):
            print("***Enter a number above or equal to {} you dangus".format(p_minimum))
        else:
            return number


def FloatWithMaximum(p_question:str, p_maximum:float):
    """
    Validates the Float that the user entered with a maximum imposed.

    Keyword arguments:
    p_question -- question posed to the user
    p_maximum -- the maximum number
    """
    while True:
        number = ValidateFloat(p_question)
        if (number > p_maximum):
            print("***Enter a number lower or equal to {} you dangus".format(p_maximum))
        else:
            return number


def FloatInsideInterval(p_question:str, p_minimum:float, p_maximum:float):
    """
    Validates the Float that the user entered with an interval imposed.

    Keyword arguments:
    p_question -- question posed to the user
    p_minimum -- the minimum number
    p_maximum -- the maximum number
    """
    while True:
        number = ValidateFloat(p_question)
        if (p_minimum > number or number > p_maximum):
            print("***Enter a number between {} and {} you dangus".format(p_minimum,p_maximum))
        else:
            return number
