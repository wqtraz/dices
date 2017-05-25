"""
Roll different types of dice and return their results.

The roll function rolls multi-faced dice.
The sroll function rolls multi-faced dice and sums them.
The adv function rolls a multi-faced die with advantage.
The dis function rolls a multi-faced die with disadvantage.
The _score function rolls a 4d6r1k3 score.
The score function rolls multiple scores.
"""

from random import randint
def roll(n, sides, modifier):
    """
    Roll multiple dice and return a list of ints.
    
    Keyword arguments:
    n -- number of dice rolled
    sides -- number of sides on the dice
    modifier -- number added to each die after rolled
    """
    return list(int(randint(1, sides) + modifier) for _ in range(n))


def sroll(n, sides, modifier):
    """
    Add dice rolls together and return an int.
    
    Keyword arguments:
    n -- number of dice rolled
    sides -- number of sides on the dice
    modifier -- number added to each die after rolled
    """
    return sum(roll(n, sides, modifier))


def adv(sides):
    """
    Roll two multi-faced dice and drop the lowest, returning an int.
    
    Keyword argument:
    sides -- number of sides on the dice
    """
    return max(roll(2, sides, 0))


def dis(sides):
    """
    Roll two multi-faced dice and drop the highest, returning an int.
    
    Keyword argument:
    sides -- number of sides on the dice
    """
    return min(roll(2, sides, 0))


def _score():
    """
    Roll an ability score by rolling 4d6r1k3 and return an int.
    
    roll four six-sided dice
    reroll ones and drop the lowest
    """
    score_roll = list(randint(2, 6) for _ in range(4))
    score_roll.remove(min(score_roll))
    return sum(score_roll)


def score(n):
    """
    Roll multiple ability scores by rolling 4d6r1k3 and return a list.
    
    Keyword argument:
    n -- number of ability scores rolled
    """
    return list(_score() for _ in range(n))

def ValidateInt(p_question:str):
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


def ValidatePositiveInt(p_question:str):
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


def ValidateNegativeInt(p_question:str):
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


def ValidateIntWithMinimum(p_question:str, p_minimum:int):
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


def ValidateIntWithMaximum(p_question:str, p_maximum:int):
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


def ValidateIntInsideInterval(p_question:str, p_minimum:int, p_maximum:int):
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

nombre = ValidateIntInsideInterval("Enter a number : ", 4, 8)
print(nombre)
