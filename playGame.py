import sys
import wordle
from tqdm import tqdm

words = [word.rstrip() for word in open('validAnswers.txt').readlines()]
allWords = [word for word in words]
data = []

index = None
answer, number = wordle.solution(index)
grid = [[" " for c in range(5)] for n in range(6)]
guesses = 0

sortedFreq = []

target = None

if len(sys.argv) == 2:
    target = sys.argv[1]


def reset(index=None):
    global words
    global data
    global grid
    global guesses
    global sortedFreq
    global answer
    global number
    words = [word.rstrip() for word in open('validAnswers.txt').readlines()]
    data = []
    answer, number = wordle.solution(index)
    grid = [[" " for c in range(5)] for n in range(6)]
    guesses = 0
    sortedFreq = []


def guess(word):
    global grid
    global guesses

    grid[guesses] = [list(word), list(wordle.check(list(answer), word))]
    guesses += 1


def checkResult():
    global grid
    for row in grid:
        if "".join(row[1]) == "ggggg":
            return True
    return False


def score(word):
    global sortedFreq
    score = 0
    used = []
    for char in word:
        for letter in sortedFreq:
            if char == letter[0] and char not in used:
                score += letter[1]
                used.append(char)
    return score


def genPossible():
    global data
    global words
    global sortedFreq
    global number
    global answer
    green = []
    for row in data:
        for i, char, color in zip(range(5), row[0], row[1]):
            # print(str(i) + " " + char + " " + color)
            if color == 'g':
                words = [word for word in words if word[i] == char]
                green.append(char)
            elif color == 'y':
                words = [word for word in words if word[i]
                         != char and char in word]
                green.append(char)
    for row in data:
        for i, char, color in zip(range(5), row[0], row[1]):
            # print(str(i) + " " + char + " " + color)
            if color == 'b':
                words = [
                    word for word in words if char not in word or char in green]
    chars = "".join(words)

    freq = []

    for letter in set(chars):
        freq.append([letter, chars.count(letter)])

    sortedFreq = [c for c in sorted(freq, key=lambda x: x[1], reverse=True)]

    words = sorted(words, key=score, reverse=True)
    if len(words) == 0:
        print(number)
        print(answer)
        return []
    return words[0]


def genData(w):
    global data
    guess(w)
    data.append([w, "".join(wordle.check(list(answer), w))])


def playGame(i, ans):
    global lost
    reset(i)
    guessList = []
    genData("arose")
    guessList.append("arose")
    if checkResult() == True:
        return [ans, guesses]
    while True:
        pos = genPossible()
        if len(pos) == 0:
            break
        genData(pos)
        guessList.append(pos)
        if guesses == 6:
            # print("Lost: " + ans + ", Number: " + str(i))
            lost.append([ans, i])
            break
        if checkResult() == True:
            # print("Won at: " + str(guesses))
            # print("The word was: " + ans)
            return [ans, guesses, guessList]


lost = []
games = []

print()
for i in tqdm(range(0, len(allWords))):
    res = playGame(i, allWords[i])
    if res:
        games.append(res)

games = [g for g in sorted(games, key=lambda x: x[1], reverse=False)]

if target == None:
    print()
    print("Won: " + str(len(games)) + "/" + str(len(allWords)) + " games")
    print()
    print("Guesses: ")

    for i in range(1, 6):
        print(" " + str(i) + " :  ", end="")
        print(len([g for g in games if g[1] == i]))

    print(">6 :  " + str(len(lost)))
    print()

# print([l[0] for l in lost])
if target != None:
    if len([g for g in lost if g[0] == target]) == 0:
        path = [g for g in games if g[0] == target][0]
        print()
        print("Guesses to make to reach 『 " + target + " 』: " + str(path[1]))
        print()
        print("Steps: ")
        for s in path[2]:
            print(s)
        print()
    else:
        print()
        print("Sorry, 『 " + target + " 』is currently not solvable ")
        print()
