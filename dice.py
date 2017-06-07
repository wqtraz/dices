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
import copy


class Initiative(list):
    def __init__(self, initiativeNb, name):
        self.initiativeNb = initiativeNb
        self.name = name


m_playerList = [] # The list that will have all the information about players and initiative
clear = lambda: os.system('cls') # You can use clear() to clear the console of all text


def RemovePlayer(p_list: list):
    """
    One option from the Initiative Tracker.
    Let's the user remove a player from the list.

    Keyword arguments:
    p_list -- a list made out of Initiative()
    """
    if (len(p_list) == 0):
        print("There's no one to remove")
    else:
        index = -1
        for player in p_list:
            index += 1
            print(" {} - Player : {} -- Initiative : {}".format(index, player.name, player.initiativeNb))
        removeIndex = val.IntInsideInterval("Pick a number from the left to remove a player : ", 0, len(p_list)-1)
        del p_list[removeIndex]


def AddPlayer(p_list: list):
    """
    One option from the Initiative Tracker.
    Let's the user add a player to the list.

    Keyword arguments:
    p_list -- a list made out of Initiative()
    """
    playerName = val.StringTrim("Enter the player's name : ")
    playerInitiative = val.Int("Enter the player's initiative : ")
    p_list.append(Initiative(playerInitiative, playerName))


def DisplayPlayerList(p_list: list):
    """
    Displays the player count and the player list.

    Keyword arguments:
    p_list -- a list made out of Initiative()
    """
    print("Number of players :", len(p_list))
    if (len(p_list) == 0):
        print(" None")
    else:
        for player in p_list:
            print(" Player : {} -- Initiative : {}".format(player.name, player.initiativeNb))


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


def InitiativeCycling(p_list: list):
    """
    Function for the "Start Initiative Cycling option".
    Tells the Game Master who's turn it is.
    """
    if (len(p_list) < 2):
        clear()
        print("Start Initiative Cycling:\nNot enough players to start.")
        spe.Wait("Return -> ")
    else:
        while True:
            clear()
            print(
"""Start Initiative Cycling:
Press [ENTER] to continue the cycle
Type [exit] to stop it.
Type [1] to add a player/monster.
Type [2] to remove a player/monster.""")
            spe.DrawLine(10, "-")
            DisplayPlayerList(p_list)
            exit = val.String("-> ")
            if (exit.lower() == "exit"):
                break
            if (exit == "1"):
                clear()
                print("Add a Player:")
                AddPlayer(p_list)
                spe.Wait("Return -> ")
            if (exit == "2"):
                clear()
                print("Remove a Player:")
                RemovePlayer(p_list)
                spe.Wait("Return -> ")

            p_list = spe.RotateList(p_list, 1)


def InitiativeTracker():
    """
    Sub-Menu for the Initiative Tracker
    """
    while True:
        clear()
        print("Initiative Tracker:")
        subChoice = val.IntInsideInterval(
"""1 - Add a Player
2 - Remove a Player
3 - Display Player List
4 - Start Initiative Cycling
0 - Return
Pick an option : """, 0, 4)

        m_playerList.sort(key=attrgetter('initiativeNb'), reverse=True) # Sort by initiative

        if (subChoice == 1):
            clear()
            print("Add a Player:")
            AddPlayer(m_playerList)
            spe.Wait("Return -> ")
        elif (subChoice == 2):
            clear()
            print("Remove a Player:")
            RemovePlayer(m_playerList)
            spe.Wait("Return -> ")
        elif (subChoice == 3):
            clear()
            print("Display Player List:")
            DisplayPlayerList(m_playerList)
            spe.Wait("Return -> ")
        elif (subChoice == 4):
            cyclingList = copy.deepcopy(m_playerList)
            InitiativeCycling(cyclingList)
        elif (subChoice == 0):
            break
        else:
            print("***Bypassed Sub-Menu restrictions.")


while True:
    clear()
    print("Main Menu:")
    choice = val.IntInsideInterval(
"""1 - Roll dice
2 - Sum roll
3 - Advantage roll
4 - Disaventage roll
5 - Ability score roll
6 - Initiative Tracker
0 - Exit
Pick an option : """, 0, 6)

    if (choice == 1):
        clear()
        print("Roll dice:")
        n = val.PositiveInt("Enter the number of dice : ")
        sides = val.PositiveInt("Enter the number of sides : ")
        modifier = val.Int("Enter the modifier : ")
        print("RESULT : ", roll(n, sides, modifier))
        spe.Wait("Return -> ")
    elif (choice == 2):
        clear()
        print("Sum roll:")
        n = val.PositiveInt("Enter the number of dice : ")
        sides = val.PositiveInt("Enter the number of sides : ")
        modifier = val.Int("Enter the modifier : ")
        print("RESULT : ", sroll(n, sides, modifier))
        spe.Wait("Return -> ")
    elif (choice == 3):
        clear()
        print("Advantage roll:")
        sides = val.PositiveInt("Enter the number of sides : ")
        modifier = val.Int("Enter the modifier : ")
        print("RESULT : ", adv(sides, modifier))
        spe.Wait("Return -> ")
    elif (choice == 4):
        clear()
        print("Disadvantage roll:")
        sides = val.PositiveInt("Enter the number of sides : ")
        modifier = val.Int("Enter the modifier : ")
        print("RESULT : ", dis(sides, modifier))
        spe.Wait("Return -> ")
    elif (choice == 5):
        clear()
        print("Ability score roll:")
        n = val.PositiveInt("Enter the number of ability score needed : ")
        print("RESULT : ", score(n))
        spe.Wait("Return -> ")
    elif (choice == 6):
        InitiativeTracker()
    elif (choice == 0):
        break
    else:
        print("***Bypassed Menu restrictions.")

spe.Wait("Press Enter to close...")


