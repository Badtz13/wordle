from cmd import Cmd
import solution
import os
import sys

validWords = [word.rstrip() for word in open('validWords.txt').readlines()]

answer, number = solution.solution()
grid = [[" " for c in range(5)] for n in range(6)]
guesses = 0


def showGrid():
    print()
    for r in grid:
        # print(r)
        printString = ""
        for i, color in enumerate(r[1]):
            if color == 'b':
                printString += "\033[1;37;40m" + r[0][i] + "\033[0m"
            elif color == 'g':
                printString += "\033[1;37;42m" + r[0][i] + "\033[0m"
            elif color == 'y':
                printString += "\033[1;37;43m" + r[0][i] + "\033[0m"
        if len(printString) > 0:
            print(printString)
    return


def check(guess):
    ans = list("".join([c for c in answer]))
    output = ['b' for i in range(5)]
    for pos, letter in enumerate(ans):
        if ans[pos] == guess[pos]:
            ans[pos] = '_'
            output[pos] = 'g'
            continue
        for gletter in guess:
            if letter == gletter:
                ans[pos] = '_'
                output[pos] = 'y'
                break
    return output


def guess(word):
    global grid
    global guesses

    grid[guesses] = [list(word), list(check(word))]

    guesses += 1


def checkResult():
    global grid
    for row in grid:
        if "".join(row[1]) == "ggggg":
            return True
    return False


def showScore():
    print("Wordle " + str(number) + " " + str(guesses) + "/6")


class prompt(Cmd):
    prompt = ''

    def do_exit(self, inp):
        print("Bye")
        return True

    def default(self, inp):
        if len(inp) != 5 or inp not in validWords:
            os.system('clear')
            showGrid()
            print("Input must be a valid 5 letter word")
        else:
            guess(inp)
            os.system('clear')
            showGrid()
            if guesses == 6:
                print("You lose!")
                print("The correct answer was: ")
                print(answer)
                sys.exit()
            elif checkResult() == True:
                print("You win!")
                showScore()
                sys.exit()


if __name__ == '__main__':
    showGrid()
    prompt().cmdloop()
