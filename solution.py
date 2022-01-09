from datetime import date
words = [word.rstrip() for word in open('validAnswers.txt').readlines()]

delta = date.today() - date(2021, 6, 19)
print(words[delta.days])
