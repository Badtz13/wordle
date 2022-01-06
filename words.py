import itertools

words = [word.rstrip() for word in open('words.txt').readlines()]
allWords = [word for word in words]

chars = "".join(words)

freq = []

for letter in set(chars):
    freq.append([letter, chars.count(letter)])

sortedFreq = [c[0] for c in sorted(freq, key=lambda x: x[1], reverse=True)]

print("Starting word count: " + str(len(words)))
print()

print("Most common letters: ")
print(sortedFreq)
print()


def removeAllMatch(five):
    global words
    for word in words:
        shouldRemove = False
        for c in five:
            if c in word:
                shouldRemove = True
        if shouldRemove:
            words.remove(word)


def findNextWord():
    global sortedFreq
    toReturn = []

    five = sortedFreq[:5]
    sortedFreq = sortedFreq[5:]

    testWords = list(
        map("".join, itertools.permutations("".join(five))))

    matchFound = False
    for w in testWords:
        if w in words:
            toReturn.append(w)
            matchFound = True

    if matchFound:
        removeAllMatch(five)
        # print(len(words))
        return(toReturn)
    else:
        return


def evaluate(w):
    scores = [0, 0, 0, 0, 0]
    for word in allWords:
        for i, char in enumerate(w):
            if char == word[i]:
                scores[i] += 1
    return(sum(scores))


bestWords = [(w, evaluate(w)) for w in findNextWord()]

print("Best words to guess, sorted by best position:")
print([c for c in sorted(bestWords, key=lambda x: x[1], reverse=True)])
