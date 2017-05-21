from random import randint
def d(sides):
    return randint(1, sides)


def adv(sides):
    return max(tuple(d(sides) for _ in range(2)))


def dis(sides):
    return min(tuple(d(sides) for _ in range(2)))


def roll(n, sides):
    return tuple(d(sides) for _ in range(n))


def score():
    scoreroll = list(randint(2, 6) for _ in range(4))
    scoreroll.remove(min(scoreroll))
    return sum(scoreroll)


def scores(n):
    return tuple(score() for _ in range(n))


def sroll(n, sides):
    return sum(list(d(sides) for _ in range(n)))

