"""
Roll different types of dice and return their results.
The d(sides) function rolls a multi-faced die.
The adv(sides) function rolls a multi-faced die with advantage.
The dis(sides) function rolls a multi-faced die with disadvantage.
The roll(n, sides) function rolls multiple multi-faced dice.
The score() function rolls 4d6r1k3.
The scores(n) function calls the score function multiple times.
The sroll(n, sides) rolls multiple multi-faced dice and sums them.
"""

from random import randint
def d(sides):
    """
    Roll a multi-faced die and return an int.
    
    Keyword argument:
    sides -- number of sides on the die
    """
    return randint(1, sides)


def adv(sides):
    """
    Roll two multi-faced dice and drop the lowest, returning an int.
    
    Keyword argument:
    sides -- number of sides on the dice
    """
    return max(tuple(d(sides) for _ in range(2)))


def dis(sides):
    """
    Roll two multi-faced dice and drop the highest, returning an int.
    
    Keyword argument:
    sides -- number of sides on the dice
    """
    return min(tuple(d(sides) for _ in range(2)))


def roll(n, sides):
    """
    Roll multiple dice and return a list.
    
    Keyword arguments:
    n -- number of dice rolled
    sides -- number of sides on the dice
    """
    return list(d(sides) for _ in range(n))


def score():
    """
    Roll an ability score by rolling 4d6r1k3 and return an int.
    
    roll four six-sided dice
    reroll ones and drop the lowest
    """
    scoreroll = list(randint(2, 6) for _ in range(4))
    scoreroll.remove(min(scoreroll))
    return sum(scoreroll)


def scores(n):
    """
    Roll multiple ability scores and return a list.
    
    Keyword argument:
    n -- number of ability scores rolled
    """
    return list(score() for _ in range(n))


def sroll(n, sides):
    """
    Add dice rolls together and return an int.
    
    Keyword arguments:
    n -- number of dice rolled
    sides -- number of sides on the dice
    """
    return sum(roll(n, sides))

def ValiderIntPositif(p_question:str):
    """Valide le Int que l'utilisateur a entré

    Keyword arguments:
    p_question -- la question qui est posé à l'utilisateur
    """
    number = 0
    while True :
        try:
            number = int(input(p_question))
            if (number < 0):
                print("***Enter a positive number you dangus")
            else:
                return number
        except Exception:
            print("***Enter a number without decimals you dangus")

nombre = ValiderIntPositif("Enter a number : ")
if (nombre != 0):
    print(d(nombre))