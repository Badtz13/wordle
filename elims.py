import itertools
allWords = [word.rstrip() for word in open('words.txt').readlines()]

possible = map(list, itertools.combinations_with_replacement([0, 1], 5))


def findElims(word, wordlist):
    for p in possible:


findElims('arose', allWords)
