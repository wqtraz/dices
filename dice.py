"""
Roll different types of dice and return their results.

The roll function rolls multi-faced dice.
The sroll function rolls multi-faced dice and sums them.
The adv function rolls a multi-faced die with advantage.
The dis function rolls a multi-faced die with disadvantage.
The _score function rolls a 4d6r1k3 score.
The score function rolls multiple scores.
"""


from operator import attrgetter
from random import randint
from util import validate as val, special as spe
import os


clear = lambda: os.system('cls') # You can use clear() to clear the console of all text

class Initiative(list):
    def __init__(self, initiativeNb, name):
        self.initiativeNb = initiativeNb
        self.name = name


m_playerList = []
m_playerCombo = Initiative("", 0)

def DisplayRemovePlayer():
    """
    Displays the name of every player.
    """
    index = -1
    for player in m_playerList:
        index += 1
        print(" {} - Player : {}".format(index, player.name))

def DisplayInitiative():
    """
    Displays the name and initiative of every player.
    """
    if (len(m_playerList) == 0):
        print(" None")
    else:
        for player in m_playerList:
            print(" Player : {} -- Initiative : {}".format(player.name, player.initiativeNb))


def DisplayPlayerCount():
    """
    Displays the player count.
    """
    print("Number of players in the Initiative Tracker :", len(m_playerList))

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


def InitiativeTracker():
    """
    Sub-Menu for the Initiative Tracker
    """
    while True:
        print("Initiative Tracker:")
        subChoice = val.IntInsideInterval(
"""1 - Add a Player
2 - Remove a Player
3 - Display Player Count
4 - Display Initiative
0 - Return
Pick an option : """, 0, 4)

        spe.DrawLine(8, '-')

        if (subChoice == 1):
            print("Add a Player:")
            playerName = val.StringTrim("Enter the player's name : ")
            playerInitiative = val.Int("Enter the player's initiative : ")
            m_playerCombo = Initiative(playerInitiative, playerName)
            m_playerList.append(m_playerCombo)
            m_playerList.sort(key=attrgetter('initiativeNb'), reverse=True) # Sort by initiative
        elif (subChoice == 2):
            print("Remove a Player:")
            if (len(m_playerList) == 0):
                print("There's no player in the Tracker")
            else:
                DisplayRemovePlayer()
                removeIndex = val.IntInsideInterval("Pick a number to remove a player : ", 0, len(m_playerList)-1)
                del m_playerList[removeIndex]
        elif (subChoice == 3):
            print("Display Player Count:")
            DisplayPlayerCount()
        elif (subChoice == 4):
            print("Display Initiative:")
            DisplayInitiative()
        elif (subChoice == 0):
            break
        else:
            print("***Bypassed Sub-Menu restrictions.")

        spe.Wait("Continue ->")
        clear()
        print(
"""1 - Roll dice
2 - Sum roll
3 - Advantage roll
4 - Disaventage roll
5 - Ability score roll
6 - Initiative Tracker
0 - Exit
Pick an option : 6""")
        spe.DrawLine(5, '-')


while True:
    choice = val.IntInsideInterval(
"""1 - Roll dice
2 - Sum roll
3 - Advantage roll
4 - Disaventage roll
5 - Ability score roll
6 - Initiative Tracker
0 - Exit
Pick an option : """, 0, 6)

    spe.DrawLine(5, '-')

    if (choice == 1):
        print("Roll dice:")
        n = val.PositiveInt("Enter the number of dice : ")
        sides = val.PositiveInt("Enter the number of sides : ")
        modifier = val.Int("Enter the modifier : ")
        print("RESULT : ", roll(n, sides, modifier))
        spe.Wait("Continue ->")
    elif (choice == 2):
        print("Sum roll:")
        n = val.PositiveInt("Enter the number of dice : ")
        sides = val.PositiveInt("Enter the number of sides : ")
        modifier = val.Int("Enter the modifier : ")
        print("RESULT : ", sroll(n, sides, modifier))
        spe.Wait("Continue ->")
    elif (choice == 3):
        print("Advantage roll:")
        sides = val.PositiveInt("Enter the number of sides : ")
        modifier = val.Int("Enter the modifier : ")
        print("RESULT : ", adv(sides, modifier))
        spe.Wait("Continue ->")
    elif (choice == 4):
        print("Disadvantage roll:")
        sides = val.PositiveInt("Enter the number of sides : ")
        modifier = val.Int("Enter the modifier : ")
        print("RESULT : ", dis(sides, modifier))
        spe.Wait("Continue ->")
    elif (choice == 5):
        print("Ability score roll:")
        n = val.PositiveInt("Enter the number of ability score needed : ")
        print("RESULT : ", score(n))
        spe.Wait("Continue ->")
    elif (choice == 6):
        InitiativeTracker()
    elif (choice == 0):
        break
    else:
        print("***Bypassed Menu restrictions.")

    clear()

spe.Wait("Press Enter to close...")


