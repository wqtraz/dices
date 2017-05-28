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
from util import validation, special

def roll(n, sides, modifier=0):
    """
    Roll multiple dice and return a list of ints.
    
    Keyword arguments:
    n -- number of dice rolled
    sides -- number of sides on the dice
    modifier -- number added to each die after rolled
    """
    return list(int(randint(1, sides) + modifier) for _ in range(n))


def sroll(n, sides, modifier=0):
    """
    Add dice rolls together and return an int.
    
    Keyword arguments:
    n -- number of dice rolled
    sides -- number of sides on the dice
    modifier -- number added to each die after rolled
    """
    return sum(roll(n, sides, modifier))


def adv(sides, modifier=0):
    """
    Roll two multi-faced dice and drop the lowest, returning an int.
    
    Keyword argument:
    sides -- number of sides on the dice
    modifier -- number added to each die after rolled
    """
    return max(roll(2, sides, modifier))


def dis(sides, modifier=0):
    """
    Roll two multi-faced dice and drop the highest, returning an int.
    
    Keyword argument:
    sides -- number of sides on the dice
    modifier -- number added to each die after rolled
    """
    return min(roll(2, sides, modifier))


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


nombreInt = validation.ValidateIntInsideInterval("Enter a number : ", 4, 8)
print(nombreInt)
nombreFloat = validation.ValidateFloatInsideInterval("Enter a number : ", 4.65 , 8.99)
print(nombreFloat)
special.Wait("Press Enter to exit...")