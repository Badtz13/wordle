import sys
import wordle
from tqdm import tqdm
validAnswers = [word.rstrip()
                for word in open('validAnswers.txt').readlines()]
validWords = [word.rstrip() for word in open('validWords.txt').readlines()]


def guess(word, answer, grid, guesses):
    grid[guesses] = [list(word), list(wordle.check(list(answer), word))]
    guesses += 1
    return grid, guesses


def checkResult(grid):
    for row in grid:
        if "".join(row[1]) == "ggggg":
            return True
    return False


def genData(w, answer):
    return[w, "".join(wordle.check(list(answer), w))]


def playGame(gameNumber, vw, va):

    data = []
    answer, _ = wordle.solution(gameNumber)
    grid = [[" " for c in range(5)] for n in range(6)]
    guesses = 0
    sortedFreq = []

    grid, guesses = guess("batch", answer, grid, guesses)
    data.append(genData("batch", answer))
    if checkResult(grid):
        return [True, answer, guesses]
    while True:
        full, some = wordle.genPossible(data, validAnswers, validWords)
        if len(some) == 1 or len(full) == 0:
            pos = some[0]
        else:
            pos = full[0]

        grid, guesses = guess(pos, answer, grid, guesses)
        data.append(genData(pos, answer))
        # print(pos)
        # print(data)

        if guesses == 6:
            if checkResult(grid):
                return [True, answer, guesses]
            else:
                return [False, answer, guesses]
        if checkResult(grid):
            return [True, answer, guesses]


games = []
for i in tqdm(range(len(validAnswers))):
    games.append([playGame(i, validAnswers, validWords), i])

games = [g for g in sorted(games, key=lambda x: x[0][2], reverse=False)]

print()
print(
    "Won: " + str(len([g for g in games if g[0][0] == True])) + "/" + str(len(games)))

lost = [g for g in games if g[0][0] == False]
print("Lost: " + str(len(lost)))
print([[l[0][1], l[1]] for l in lost])

print()
print("Guesses: ")

for i in range(1, 7):
    print(" " + str(i) + " :  ", end="")
    print(len([g for g in games if g[0][2] == i]))

print(">6 :  " + str(len(lost)))
print()
