import itertools
from tqdm import tqdm

words = [word.rstrip() for word in open('validAnswers.txt').readlines()]
everyWord = [word.rstrip() for word in open('validWords.txt').readlines()]

scores = []


def check(answer, guess):
    output = ['b' for i in range(5)]
    for pos, letter in enumerate(answer):
        if answer[pos] == guess[pos]:
            answer[pos] = '_'
            output[pos] = 'g'
            continue
        for gletter in guess:
            if letter == gletter:
                answer[pos] = '_'
                output[pos] = 'y'
                break
    return output


def getScore(word):
    score = 0
    for w in everyWord:
        for s in check(list(word), list(w)):
            if s == 'g':
                score += 10
            elif s == 'y':
                score += 6
            else:
                score -= 2
    return score


for word in tqdm([w for w in everyWord if len(set(w)) == 5]):
    scores.append([word, getScore(list(word))])

print([c for c in sorted(scores, key=lambda x: x[1], reverse=True)][:10])
