import sys
words = [word.rstrip() for word in open('words.txt').readlines()]

if len(sys.argv) != 3:
    print("usage: python match.py <letters it has> <letters it doesnt>")
    sys.exit()
else:
    has = list(sys.argv[1])
    doesnt = list(sys.argv[2])


def keep(w):
    for char in doesnt:
        if char in w:
            return False
    return True


words = [word for word in words if keep(word)]

possible = []
for word in words:
    should = len(has)
    for c in has:
        if c in word:
            should -= 1
    if should < 1:
        possible.append(word)

print("Possible words are:")
print(possible)

chars = "".join(possible)

freq = []

for letter in set(chars):
    freq.append([letter, chars.count(letter)])

sortedFreq = [c[0] for c in sorted(freq, key=lambda x: x[1], reverse=True)]

print()
print("Best letters to guess by frequency, excluding letters you already have:")
print([c for c in sortedFreq if c not in has])
