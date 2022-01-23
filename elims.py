import json
import math

from tqdm import tqdm

words = [word.rstrip() for word in open('validAnswers.txt').readlines()]
everyWord = [word.rstrip() for word in open('validWords.txt').readlines()]


def generateMaskPerms(guessList, answerList):
    maskDict = {}
    bar = tqdm(guessList)
    for guess in bar:
        bar.set_description(guess, refresh=True)
        maskDict[guess] = {}
        for answer in answerList:
            mask = check(list(answer), guess)
            if mask not in maskDict[guess]:
                maskDict[guess][mask] = 0
            maskDict[guess][mask] += 1
    with open('maskDict.json', 'w') as maskFile:
        maskFile.write(json.dumps(maskDict))


def modifyWordList(wordlist, mask, guess):
    modifiedWordList = wordlist
    for pos, color, character in zip(range(len(mask)), mask, guess):
        if color == 'b':
            modifiedWordList = [
                word for word in modifiedWordList if character not in word]
        elif color == 'y':
            modifiedWordList = [
                word for word in modifiedWordList if character in word and word[pos] != character]
        elif color == 'g':
            modifiedWordList = [
                word for word in modifiedWordList if word[pos] == character]
    return modifiedWordList


def bestWord(maskDict, answerList):
    bestWord = ""
    bestWordLen = math.inf
    bar = tqdm(maskDict.items())
    for word, masks in bar:
        wordListLen = 0
        for mask, frequency in masks.items():
            modifiedWordList = modifyWordList(answerList, mask, word)
            wordListLen += len(modifiedWordList) * frequency
        if wordListLen < bestWordLen:
            bestWord = word
            bar.set_description(bestWord, refresh=True)
            bestWordLen = wordListLen

    return bestWord


# answer = "__ery"
# guess = "quote"
# output = "ggbbb"


def check(answer, guess):
    output = ['b' for i in range(5)]
    for pos, letter in enumerate(answer):
        # print(f"{letter}")
        if answer[pos] == guess[pos]:
            answer[pos] = '_'
            output[pos] = 'g'
            # print(f"\tGreen!")
            continue
        for i, gletter in enumerate(guess):
            # print(f"\t{gletter}")
            if letter == gletter:
                # print(f"\tYellow!")
                answer[i] = '_'
                output[i] = 'y'
                break
    return "".join(output)


print(check(list("query"), "quote"))
# # print(check(list("truss"), "ssurt"))
# generateMaskPerms(everyWord, words)
# with open('maskDict.json', 'r') as maskFile:
#     maskDict = json.load(maskFile)
#     bestWord(maskDict, words)
