import wordle
import sys

validAnswers = [word.rstrip() for word in open('validAnswers.txt').readlines()]
validWords = [word.rstrip() for word in open('validWords.txt').readlines()]

data = []

args = sys.argv[1:]
if len(args) < 2:
    print("usage: python match.py <word guessed> <colors>, <word guessed> <colors>, ...")
    sys.exit()
else:
    for i in range(0, len(args), 2):
        data.append([args[i], args[i+1]])

full, some = wordle.genPossible(data, validAnswers, validWords)
print(full[:10])
print(some[:10])
