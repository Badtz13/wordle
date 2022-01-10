from datetime import date
words = [word.rstrip() for word in open('validAnswers.txt').readlines()]


def solution():
    delta = date.today() - date(2021, 6, 19)
    return words[delta.days], delta.days
