from cmd import Cmd
import solution
import os
import sys

validWords = [word.rstrip() for word in open('validWords.txt').readlines()]

index = None

if len(sys.argv) > 1:
    index = int(sys.argv[1])

answer, number = solution.solution(index)
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


def check(answer, guess):
    output = ['b' for i in range(5)]
    for pos, letter in enumerate(answer):
        # print(f"{letter}")
        if answer[pos] == guess[pos]:
            answer[pos] = '_'
            output[pos] = 'g'
            # print(f"\tGreen!")
            continue
        for i, gletter in enumerate(guess):
            # print(f"\t{gletter}")
            if letter == gletter:
                # print(f"\tYellow!")
                answer[i] = '_'
                output[i] = 'y'
                break
    return output


def guess(word):
    global grid
    global guesses

    grid[guesses] = [list(word), list(check(list(answer), word))]

    guesses += 1


def checkResult():
    global grid
    for row in grid:
        if "".join(row[1]) == "ggggg":
            return True
    return False


def showScore():
    global grid
    print()
    print("Wordle " + str(number) + " " + str(guesses) + "/6")
    print()
    for row in grid:
        rowString = []
        for c in row[1]:
            if c == 'g':
                rowString.append('🟩')
            elif c == 'y':
                rowString.append('🟨')
            elif c == 'b':
                rowString.append('⬛')
        if len(rowString) > 0:
            print("".join(rowString))
    print()


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
                showScore()
                return True


if __name__ == '__main__':
    showGrid()
    prompt().cmdloop()
