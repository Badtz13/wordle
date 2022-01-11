from datetime import date
words = [word.rstrip() for word in open('validAnswers.txt').readlines()]


def solution(day=None):
    days = day if day else (date.today() - date(2021, 6, 19)).days
    return words[days], days
