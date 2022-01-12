import sys
words = [word.rstrip() for word in open('validAnswers.txt').readlines()]

data = []

args = sys.argv[1:]
if len(args) < 2:
    print("usage: python match.py <word guessed> <colors>, <word guessed> <colors>, ...")
    sys.exit()
else:
    for i in range(0, len(args), 2):
        data.append([args[i], args[i+1]])


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


green = []

for row in data:
    for i, char, color in zip(range(5), row[0], row[1]):
        print(str(i) + " " + char + " " + color)
        if color == 'g':
            words = [word for word in words if word[i] == char]
            green.append(char)
        elif color == 'y':
            words = [word for word in words if word[i]
                     != char and char in word]
            green.append(char)
        print(words)

for row in data:
    for i, char, color in zip(range(5), row[0], row[1]):
        print(str(i) + " " + char + " " + color)
        if color == 'b':
            words = [
                word for word in words if char not in word or char in green]
        print(words)

chars = "".join(words)

freq = []

for letter in set(chars):
    freq.append([letter, chars.count(letter)])

sortedFreq = [c for c in sorted(freq, key=lambda x: x[1], reverse=True)]

print()
print("Best letters to guess by frequency: ")
print(sortedFreq)


words = sorted(words, key=score, reverse=True)

print()
print("Best words to guess by frequency, excluding impossible words: ")
print(words)
