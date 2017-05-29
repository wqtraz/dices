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
from util import validate as val, special as spe
import os

def roll(n: int, sides: int, modifier: int = 0):
    """
    Roll multiple dice and return a list of ints.
    
    Keyword arguments:
    n -- number of dice rolled
    sides -- number of sides on the dice
    modifier -- number added to each die after rolled
    """
    return list((randint(1, sides) + modifier) for _ in range(n))


def sroll(n: int, sides: int, modifier: int = 0):
    """
    Add dice rolls together and return an int.
    
    Keyword arguments:
    n -- number of dice rolled
    sides -- number of sides on the dice
    modifier -- number added to each die after rolled
    """
    return (sum(roll(n, sides, 0)) + modifier)


def adv(sides: int, modifier: int = 0):
    """
    Roll two multi-faced dice and drop the lowest, returning an int.
    
    Keyword argument:
    sides -- number of sides on the dice
    modifier -- number added to each die after rolled
    """
    return max(roll(2, sides, modifier))


def dis(sides: int, modifier: int = 0):
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


def score(n: int):
    """
    Roll multiple ability scores by rolling 4d6r1k3 and return a list.
    
    Keyword argument:
    n -- number of ability scores rolled
    """
    return list(_score() for _ in range(n))



n = 1
sides = 1
modifier = 0
clear = lambda: os.system('cls') # You can use clear() to clear the console of all text

while True:
    choice = val.IntInsideInterval(
"""1 - Roll dice
2 - Sum roll
3 - Advantage roll
4 - Disadventage roll
5 - Ability score roll
0 - Exit
Pick an option : """, 0, 5)

    spe.DrawLine(5)

    if (choice == 1):
        print("Roll dice command:")
        n = val.PositiveInt("Enter the number of dice : ")
        sides = val.PositiveInt("Enter the number of sides : ")
        modifier = val.Int("Enter the modifier : ")
        print("RESULT : ", roll(n, sides, modifier))
    elif (choice == 2):
        print("Sum roll command:")
        n = val.PositiveInt("Enter the number of dice : ")
        sides = val.PositiveInt("Enter the number of sides : ")
        modifier = val.Int("Enter the modifier : ")
        print("RESULT : ", sroll(n, sides, modifier))
    elif (choice == 3):
        print("Advantage roll command:")
        sides = val.PositiveInt("Enter the number of sides : ")
        modifier = val.Int("Enter the modifier : ")
        print("RESULT : ", adv(sides, modifier))
    elif (choice == 4):
        print("Disadvantage roll command:")
        sides = val.PositiveInt("Enter the number of sides : ")
        modifier = val.Int("Enter the modifier : ")
        print("RESULT : ", dis(sides, modifier))
    elif (choice == 5):
        print("Ability score roll command:")
        n = val.PositiveInt("Enter the number of ability score needed : ")
        print("RESULT : ", score(n))
    elif (choice == 0):
        break
    else:
        print("***Not supposed to be here.")

    spe.Wait("Continue ->")
    clear()

spe.Wait("Press Enter to close...")


