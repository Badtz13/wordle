from cmd import Cmd
import wordle
import os
import sys

validWords = [word.rstrip() for word in open('validWords.txt').readlines()]

index = None

if len(sys.argv) > 1:
    index = int(sys.argv[1])

answer, number = wordle.solution(index)
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
                printString += "\033[1;32;40m" + r[0][i] + "\033[0m"
            elif color == 'y':
                printString += "\033[1;33;40m" + r[0][i] + "\033[0m"
        if len(printString) > 0:
            print(printString)
    return


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
                return True
            elif checkResult() == True:
                print("You win!")
                wordle.showScore(grid, number, guesses)
                return True


if __name__ == '__main__':
    # print(check(list("abbey"), "ables"))
    showGrid()
    prompt().cmdloop()
