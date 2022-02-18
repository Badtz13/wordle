import sys

import wordle

data = []

args = sys.argv[1:]
if len(args) < 2:
    print("usage: python match.py <word guessed> <colors>, <word guessed> <colors>, ...")
    sys.exit()
else:
    for i in range(0, len(args), 2):
        data.append([args[i], args[i+1]])

full, some = wordle.genPossible(
    data, wordle.validAnswers(), wordle.validWords())
print(full[:10])
print(some[:10])
