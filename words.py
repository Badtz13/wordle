import itertools

words = [word.rstrip() for word in open('words.txt').readlines()]

chars = "".join(words)

freq = []

for letter in set(chars):
    freq.append([letter, chars.count(letter)])

sortedFreq = [c[0] for c in sorted(freq, key=lambda x: x[1], reverse=True)]

print("Starting word count: " + str(len(words)))
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

    five = sortedFreq[:5]
    sortedFreq = sortedFreq[5:]
    print(five)
    testWords = list(
        map("".join, itertools.permutations("".join(five))))

    matchFound = False
    for w in testWords:
        if w in words:
            print(w)
            matchFound = True

    if matchFound:
        removeAllMatch(five)
        print(len(words))
        print()
    else:
        return


findNextWord()
findNextWord()
findNextWord()
findNextWord()
