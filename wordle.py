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
                # guess[i] = '_'
                output[i] = 'y'
                break
    return output


def score(word, freqList):
    score = 0
    used = []
    for char in word:
        for letter in freqList:
            if char == letter[0] and char not in used:
                score += letter[1]
                used.append(char)
    return score


def genPossible(data, validWords, validAnswers):
    green = []
    words = [word for word in validWords]
    guessList = [g[0] for g in data]

    for row in data:
        for i, char, color in zip(range(5), row[0], row[1]):
            if color == 'g':
                words = [word for word in words if word[i] == char]
                green.append(char)
            elif color == 'y':
                words = [word for word in words if word[i]
                         != char and char in word]
                green.append(char)

    for row in data:
        for i, char, color in zip(range(5), row[0], row[1]):
            if color == 'b':
                words = [
                    word for word in words if char not in word or char in green]

    chars = "".join(words)

    freq = []

    for letter in set(chars):
        freq.append([letter, chars.count(letter)])

    sortedFreq = [c for c in sorted(freq, key=lambda x: x[1], reverse=True)]
    sortedFreq = [c for c in sortedFreq if c[0] not in green]
    if len(sortedFreq) != 0:

        wordScores = []
        for word in validWords:
            wordScores.append([word, score(word, sortedFreq)])

        full = [w[0] for w in sorted(
            wordScores, key=lambda x: x[1], reverse=True)]
    else:
        full = []

    some = sorted(words, key=lambda x: score(x[1], sortedFreq), reverse=True)

    return [w for w in full if w not in guessList], [w for w in some if w not in guessList]
