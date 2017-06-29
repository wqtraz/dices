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
import ctypes


class bcolors:
    """
    A class that lets you use colors in the console.

    HEADER is purple.
    OKBLUE is dark blue.
    OKGREEN is green.
    WARNING is yellow.
    FAIL is red.
    ENDC is the normal color. You use this after using any color.
    BOLD is white.
    UNDERLINE underlines text.
    """
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    # Credits: https://stackoverflow.com/questions/287871/print-in-terminal-with-colors-using-python


class Initiative(list):
    def __init__(self, initiativeNb, name):
        self.initiativeNb = initiativeNb
        self.name = name


m_playerList = [] # The list that will have all the information about players and initiative
clear = lambda: os.system('cls') # You can use clear() to clear the console of all text
os.system('mode con: cols=90 lines=30') # Resizing the console
ctypes.windll.kernel32.SetConsoleTitleW("Dices (made with Python)")


def About():
    """
    The About of this program.
    """
    clear()
    print(bcolors.HEADER + "About:" + bcolors.ENDC + 
"""
This program was made by:
    wqtraz (on GitHub)
    DAgostinateur (on GitHub)

This program is a utility for running D&D 5th edition games.""")
    spe.Wait("Return -> ")


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


def RemovePlayer(p_list: list):
    """
    One option from the Initiative Tracker.
    Let's the user remove a player from the list.

    Keyword arguments:
    p_list -- a list made out of Initiative()
    """
    print(bcolors.HEADER + "Remove a Player:" + bcolors.ENDC)
    if (len(p_list) == 0):
        print(bcolors.WARNING + "There's no one to remove" + bcolors.ENDC)
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
    print(
bcolors.HEADER + "Add a Player:" + bcolors.ENDC +
"""
1 - Roll Initiative
2 - Enter Initiative manually""")
    rollChoice = val.IntInsideInterval("Pick an Option : ", 1, 2)
    spe.DrawLine(10, "-")

    if (rollChoice == 1):
        playerName = val.StringTrim("Enter the player's name : ")
        playerModifier = val.Int("Enter the player's initiative modifier : ")
        playerInitiative = str(roll(1, 20, playerModifier))
        playerInitiative = int(playerInitiative[1:len(playerInitiative)-1])
        print("Initiative :", playerInitiative) # Removing the [] from the result
        p_list.append(Initiative(playerInitiative, playerName))
    elif (rollChoice == 2):
        playerName = val.StringTrim("Enter the player's name : ")
        playerInitiative = val.Int("Enter the player's initiative : ")
        p_list.append(Initiative(playerInitiative, playerName))
    else:
        print(bcolors.FAIL + "***Bypassed restrictions." + bcolors.ENDC)


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
        firstDetector = 0
        for player in p_list:
            firstDetector += 1
            if (firstDetector == 1):
                print(bcolors.OKGREEN + " Player : {} -- Initiative : {}".format(player.name, player.initiativeNb) + bcolors.ENDC)
            else:
                print(" Player : {} -- Initiative : {}".format(player.name, player.initiativeNb))


def DiceRolling():
    """
    Sub-Menu for the Dice Rolling
    """
    while True:
        clear()
        print(
    bcolors.HEADER + "Dice Rolling:" + bcolors.ENDC +
"""
1 - Roll dice
2 - Sum roll
3 - Advantage roll
4 - Disaventage roll
5 - Ability score roll
0 - Return""")
        choice = val.IntInsideInterval("Pick an option : ", 0, 5)

        if (choice == 1):
            clear()
            print(bcolors.HEADER + "Roll dice:" + bcolors.ENDC)
            n = val.PositiveInt("Enter the number of dice : ")
            sides = val.PositiveInt("Enter the number of sides : ")
            modifier = val.Int("Enter the modifier : ")
            print("RESULT : ", roll(n, sides, modifier))
            spe.Wait("Return -> ")
        elif (choice == 2):
            clear()
            print(bcolors.HEADER + "Sum roll:" + bcolors.ENDC)
            n = val.PositiveInt("Enter the number of dice : ")
            sides = val.PositiveInt("Enter the number of sides : ")
            modifier = val.Int("Enter the modifier : ")
            print("RESULT : ", sroll(n, sides, modifier))
            spe.Wait("Return -> ")
        elif (choice == 3):
            clear()
            print(bcolors.HEADER + "Advantage roll:" + bcolors.ENDC)
            sides = val.PositiveInt("Enter the number of sides : ")
            modifier = val.Int("Enter the modifier : ")
            print("RESULT : ", adv(sides, modifier))
            spe.Wait("Return -> ")
        elif (choice == 4):
            clear()
            print(bcolors.HEADER + "Disadvantage roll:" + bcolors.ENDC)
            sides = val.PositiveInt("Enter the number of sides : ")
            modifier = val.Int("Enter the modifier : ")
            print("RESULT : ", dis(sides, modifier))
            spe.Wait("Return -> ")
        elif (choice == 5):
            clear()
            print(bcolors.HEADER + "Ability score roll:" + bcolors.ENDC)
            n = val.PositiveInt("Enter the number of ability score needed : ")
            print("RESULT : ", score(n))
            spe.Wait("Return -> ")
        elif (choice == 0):
            break
        else:
            print(bcolors.FAIL + "***Bypassed restrictions." + bcolors.ENDC)


def InitiativeCycling(p_list: list):
    """
    Function for the "Start Initiative Cycling option".
    Tells the Game Master who's turn it is.
    """
    if (len(p_list) < 2):
        clear()
        print(bcolors.HEADER + "Start Initiative Cycling:" + bcolors.WARNING + "\nNot enough players to start." + bcolors.ENDC)
        spe.Wait("Return -> ")
    else:
        while True:
            clear()
            print(
bcolors.HEADER + "Start Initiative Cycling:" + bcolors.ENDC +
"""
Press [ENTER] to continue the cycle
Type [exit] to stop it.
Type [1] to add a player/monster.
Type [2] to remove a player/monster.
Type [3] to roll dice.""")
            spe.DrawLine(10, "-")
            DisplayPlayerList(p_list)
            exit = val.StringTrim("-> ")
            if (exit.lower() == "exit"):
                break
            elif (exit == "1"):
                clear()
                AddPlayer(p_list)
                spe.Wait("Return -> ")
            elif (exit == "2"):
                clear()
                RemovePlayer(p_list)
                spe.Wait("Return -> ")
            elif (exit == "3"):
                clear()
                DiceRolling()
            elif (exit == ""):
                p_list = spe.RotateList(p_list, 1)
            else:
                pass


def InitiativeTracker():
    """
    Sub-Menu for the Initiative Tracker
    """
    while True:
        clear()
        print(
bcolors.HEADER + "Initiative Tracker:" + bcolors.ENDC +
"""
1 - Add a Player
2 - Remove a Player
3 - Clear Player List
4 - Display Player List
5 - Start Initiative Cycling
0 - Return""")
        subChoice = val.IntInsideInterval("Pick an option : ", 0, 5)
        m_playerList.sort(key=attrgetter('initiativeNb'), reverse=True) # Sort by initiative

        if (subChoice == 1):
            clear()
            AddPlayer(m_playerList)
            spe.Wait("Return -> ")
        elif (subChoice == 2):
            clear()
            RemovePlayer(m_playerList)
            spe.Wait("Return -> ")
        elif (subChoice == 3):
            clear()
            print(bcolors.HEADER + "Clear Player List:" + bcolors.OKGREEN + "\nList cleared." + bcolors.ENDC)
            del m_playerList[:] # Deletes everything in the list
            spe.Wait("Return -> ")
        elif (subChoice == 4):
            clear()
            print(bcolors.HEADER + "Display Player List:" + bcolors.ENDC)
            DisplayPlayerList(m_playerList)
            spe.Wait("Return -> ")
        elif (subChoice == 5):
            cyclingList = copy.deepcopy(m_playerList)
            InitiativeCycling(cyclingList)
        elif (subChoice == 0):
            break
        else:
            print(bcolors.FAIL + "***Bypassed restrictions." + bcolors.ENDC)


while True:
    clear()
    print(
bcolors.HEADER + "Main Menu:" + bcolors.ENDC +
"""
1 - Dice Rolling
2 - Initiative Tracker
3 - About
0 - Exit""")
    choice = val.IntInsideInterval("Pick an option : ", 0, 3)

    if (choice == 1):
        DiceRolling()
    elif (choice == 2):
        InitiativeTracker()
    elif (choice == 3):
        About()
    elif (choice == 0):
        break
    else:
        print(bcolors.FAIL + "***Bypassed restrictions." + bcolors.ENDC)

spe.Wait("Press Enter to close...")