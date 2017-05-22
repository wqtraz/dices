from random import randint
def d(sides):
    """Roll a die.
    
    Keyword argument:
    sides -- number of sides on the die
    """
    return randint(1, sides)


def adv(sides):
    """Roll two dice and drop the lowest.
    
    Keyword argument:
    sides -- number of sides on the dice
    """
    return max(tuple(d(sides) for _ in range(2)))


def dis(sides):
    """Roll two dice and drop the highest.
    
    Keyword argument:
    sides -- number of sides on the dice
    """
    return min(tuple(d(sides) for _ in range(2)))


def roll(n, sides):
    """Roll multiple dice.
    
    Keyword arguments:
    n -- number of dice rolled
    sides -- number of sides on the dice
    """
    return tuple(d(sides) for _ in range(n))


def score():
    """Roll an ability score.
    
    roll four six-sided dice
    reroll ones and drop the lowest
    """
    scoreroll = list(randint(2, 6) for _ in range(4))
    scoreroll.remove(min(scoreroll))
    return sum(scoreroll)


def scores(n):
    """Roll multiple ability scores.
    
    Keyword argument:
    n -- number of ability scores rolled
    """
    return tuple(score() for _ in range(n))


def sroll(n, sides):
    """Add dice rolls together.
    
    Keyword arguments:
    n -- number of dice rolled
    sides -- number of sides on the dice
    """
    return sum(roll(n, sides))

