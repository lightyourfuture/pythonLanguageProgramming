from random import random


def printIntro():
    """
    Prints an introduction to the program that simulates a sports competition between two players, A and B.
    The program requires the ability values of players A and B (represented as decimal numbers between 0 and 1).
    """
    print("这个程序模拟两个选手A和B的某种竞技比赛")
    print("程序运行需要A和B的能力值(以0到1之间的小数表示)")


def getInputs():
    """
    Prompts the user to enter the ability value for player A.
    Returns the entered value as a float.
    """
    a = eval(input("请输入选手A的能力值(0-1): "))
    b = eval(input("请输入选手B的能力值(0-1): "))
    n = eval(input("模拟比赛的场次: "))
    return a, b, n


def printSummary(winsA, winsB):
    """
    Simulates a single game of a sports competition between two players, A and B.
    Takes the probability of player A winning a point (probA) and the probability of player B winning a point (probB) as arguments.
    Returns the final scores of players A and B as a tuple.
    """
    n = winsA + winsB
    print("竞技分析开始，共模拟{}场比赛".format(n))
    print("选手A获胜{}场比赛，占比{:.1%}".format(winsA, winsA / n))
    print("选手B获胜{}场比赛，占比{:.1%}".format(winsB, winsB / n))


def simOneGame(probA, probB):
    """
    Simulates a single game of a sports competition between two players, A and B.
    Takes the probability of player A winning a point (probA) and the probability of player B winning a point (probB) as arguments.
    Returns the final scores of players A and B as a tuple.
    """
    scoreA, scoreB = 0, 0
    serving = "A"
    while not gameOver(scoreA, scoreB):
        if serving == "A":
            if random() < probA:
                scoreA += 1
            else:
                serving = "B"
        else:
            if random() < probB:
                scoreB += 1
            else:
                serving = "A"
    return scoreA, scoreB


def simNGames(n, probA, probB):
    """
    Simulates a series of n games of a sports competition between two players, A and B.
    Takes the number of games to simulate (n), the probability of player A winning a point (probA), and the probability of player B winning a point (probB) as arguments.
    Returns the number of games won by player A and player B as a tuple.
    """
    winsA, winsB = 0, 0
    for i in range(n):
        scoreA, scoreB = simOneGame(probA, probB)
        if scoreA > scoreB:
            winsA += 1
        else:
            winsB += 1
    return winsA, winsB


def gameOver(a, b):
    """
    Checks if the game is over based on the scores of players A and B.
    Takes the scores of players A (a) and B (b) as arguments.
    Returns True if either player has reached a score of 15, indicating the end of the game. Otherwise, returns False.
    """
    return a == 15 or b == 15


def main():
    """
    Executes the main logic of the program.
    Calls the necessary functions to print the introduction, get user inputs for player probabilities, simulate a series of games, and print the summary of game results.
    """
    printIntro()
    probA, probB, n = getInputs()
    winsA, winsB = simNGames(n, probA, probB)
    printSummary(winsA, winsB)


# Run the program
if __name__ == "__main__":
    main()
