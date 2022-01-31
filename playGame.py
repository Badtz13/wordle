#!/usr/bin/env python
import sys

from tqdm import tqdm

import wordle

# read in lists
validAnswers = [word.rstrip()
                for word in open('validAnswers.txt').readlines()]
validWords = [word.rstrip() for word in open('validWords.txt').readlines()]


def guess(word, answer, grid, guesses, guessList):
    # guesses a word and returns the new grid and guess count
    grid[guesses] = [list(word), list(wordle.check(list(answer), word))]
    guessList.append(word)
    guesses += 1
    return grid, guesses, guessList


def checkResult(grid, guesses):
    # checks if the most recent guess won the game
    if "".join(grid[guesses-1][1]) == "ggggg":
        return True
    return False


def playGame(answer, vw, va, firstGuess=wordle.bestFirstWord()):
    # plays the game, given the answer and wordlists

    # reset variables
    data = []
    grid = [[" " for c in range(5)] for n in range(6)]
    guesses = 0
    guessList = []
    sortedFreq = []

    # guess the first guess
    grid, guesses, guessList = guess(
        firstGuess, answer, grid, guesses, guessList)
    data.append([firstGuess, "".join(wordle.check(list(answer), firstGuess))])

    # make sure it didnt win instantly
    if checkResult(grid, guesses):
        return [True, answer, guesses]

    # basic game loop
    while True:

        # find possible words
        full, some = wordle.genPossible(data, validAnswers, validWords)

        # if there is only one possible answer, select it
        if len(some) < 3 or len(full) == 0:
            selected = some[0]
        else:
            selected = full[0]

        # guess the selected word
        grid, guesses, guessList = guess(
            selected, answer, grid, guesses, guessList)
        data.append([selected, "".join(wordle.check(list(answer), selected))])

        # check if we won
        if checkResult(grid, guesses):
            return [True, answer, guesses, guessList, grid]

        # make sure we didn't lose before looping
        if guesses == 6:
            return [False, answer, guesses, guessList, grid]


def showUsage():
    print("Usage:")
    print("newGame.py all")
    print("newGame.py single <today/gameNumber>")
    print("newGame.py findBest <divisor> <segment>")


# no args, show help
if len(sys.argv) == 1:
    showUsage()

# if multiple args
elif len(sys.argv) > 1:
    command = sys.argv[1]

    # play single game
    if command == "single":

        # check if game number is specified
        if len(sys.argv) > 2:
            word, number = wordle.solution(int(sys.argv[2]))

        # assume today
        else:
            word, number = wordle.solution()

        result = playGame(word, validAnswers, validWords)
        print("Wins in " + str(result[2]) + " guesses: ")
        print(result[3])
        wordle.showScore(result[4], number, result[2])
    elif command == "all":
        startWord = wordle.bestFirstWord()
        if len(sys.argv) == 3:
            startWord = sys.argv[2]

        games = []
        for i in tqdm(range(len(validAnswers))):
            games.append(
                [playGame(validAnswers[i], validAnswers, validWords, startWord), i])

        games = [g for g in sorted(
            games, key=lambda x: x[0][2], reverse=False)]

        # show results
        print()
        print(
            "Won: " + str(len([g for g in games if g[0][0] == True])) + "/" + str(len(games)))

        lost = [g for g in games if g[0][0] == False]
        print("Lost: " + str(len(lost)))

        # show names of lost games, if any
        if len(lost) > 0:
            print([[l[0][1], l[1]] for l in lost])

        # guess count output
        print()
        print("Guesses: ")
        for i in range(1, 7):
            print(" " + str(i) + " :  ", end="")
            print(len([g for g in games if g[0][2] == i]))

        print(">6 :  " + str(len(lost)))
        print()
    elif command == "findBest":

        # check for list size?
        if len(sys.argv) == 4:
            segment = int(sys.argv[3])
            segSize = len(validWords) // int(sys.argv[2])

            validWords = [validWords[i]
                          for i in range(segment*segSize, segSize*(segment+1))]

            print("Checking all possible starting words: ")
            doneScores = [w.rstrip().split(",")
                          for w in open('doneGames.txt').readlines()]
            doneWords = [w[0] for w in doneScores]
            doneFile = open("doneGames.txt", "a")
            if len(doneWords) > 0:
                print(str(len(doneWords)) +
                      " completed words found, removing from segment and resuming... ")

            validWords = [c for c in validWords if c not in doneWords]

            print(str(len(validWords)) +
                  " words left to try in the specified segment ")

            if(len(validWords) == 0):
                print("This segment is already completed!")
                sys.exit()

            allGames = []
            for w in tqdm(validWords):
                shouldBreak = False
                # play games and show progress bar
                games = []
                for i in tqdm(range(len(validAnswers))):
                    tempRes = [
                        playGame(validAnswers[i], validAnswers, validWords, w), i]
                    if tempRes[0] == False:
                        shouldBreak = True
                        break
                    games.append(tempRes)
                if shouldBreak:
                    doneFile.write(w + ",10\n")
                    continue

                points = []

                for i in range(1, 7):
                    points += [g[0][2] for g in games if g[0][2] == i]
                allGames.append(
                    [True, w, round(sum(points)/len(points), 3)])
                doneFile.write(
                    w + "," + str(round(sum(points)/len(points), 3)) + "\n")

            allGames = [g for g in allGames if g[0] == True]
            allGames = [[g[1], g[2]] for g in allGames]
            allGames += doneScores
            allGames = [g for g in sorted(
                allGames, key=lambda x: float(x[1]), reverse=False)]

            print(allGames[:3])
