import sys
import wordle
from tqdm import tqdm

# read in lists
validAnswers = [word.rstrip()
                for word in open('validAnswers.txt').readlines()]
validWords = [word.rstrip() for word in open('validWords.txt').readlines()]


def guess(word, answer, grid, guesses):
    # guesses a word and returns the new grid and guess count
    grid[guesses] = [list(word), list(wordle.check(list(answer), word))]
    guesses += 1
    return grid, guesses


def checkResult(grid, guesses):
    # checks if the most recent guess won the game
    if "".join(grid[guesses-1][1]) == "ggggg":
        return True
    return False


def playGame(answer, vw, va):
    # plays the game, given the answer and wordlists

    # reset variables
    data = []
    grid = [[" " for c in range(5)] for n in range(6)]
    guesses = 0
    sortedFreq = []
    firstGuess = "batch"

    # guess the first guess
    grid, guesses = guess(firstGuess, answer, grid, guesses)
    data.append([firstGuess, "".join(wordle.check(list(answer), firstGuess))])

    # make sure it didnt win instantly
    if checkResult(grid, guesses):
        return [True, answer, guesses]

    # basic game loop
    while True:

        # find possible words
        full, some = wordle.genPossible(data, validAnswers, validWords)

        # if there is only one possible answer, select it
        if len(some) == 1 or len(full) == 0:
            selected = some[0]
        else:
            selected = full[0]

        # guess the selected word
        grid, guesses = guess(selected, answer, grid, guesses)
        data.append([selected, "".join(wordle.check(list(answer), selected))])

        # check if we won
        if checkResult(grid, guesses):
            return [True, answer, guesses]

        # make sure we didn't lose before looping
        if guesses == 6:
            return [False, answer, guesses]


# play games and show progress bar
games = []
for i in tqdm(range(len(validAnswers))):
    games.append([playGame(validAnswers[i], validAnswers, validWords), i])

games = [g for g in sorted(games, key=lambda x: x[0][2], reverse=False)]


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
