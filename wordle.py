from datetime import date
words = [word.rstrip() for word in open('validAnswers.txt').readlines()]


def solution(day=None):
    days = day if day else (date.today() - date(2021, 6, 19)).days
    return words[days], days


def check(answer, guessStr):
    guess = list(guessStr)
    output = ['b' for i in range(5)]
    for pos, letter in enumerate(answer):
        # print(f"{letter}")
        if answer[pos] == guess[pos]:
            answer[pos] = ' '
            guess[pos] = '_'
            output[pos] = 'g'
            # print(f"\tGreen!")
            continue
        for i, gletter in enumerate(guess):
            # print(f"\t{gletter}")
            if letter == gletter:
                # print(f"\tYellow!")
                answer[pos] = ' '
                guess[i] = '_'
                output[i] = 'y'
                break
    return output
