# Wordle Tools
Contains various tools and experiments related to the recently popular online word game [wordle](https://www.powerlanguage.co.uk/wordle/)

## Files

 
| File Name        | Description                                                           |
| ---------------- | ----------------------------------------------------------------------|
| site/            | Contains a local version of the wordle site                           |
| elims.py         | Calculates which words eliminate the most words                       |
| game.py          | A cli version of wordle                                               |
| match.py         | A tool used to help solve wordles during solve                        |
| playGame.py      | Uses the same logic as match.py to try win all games                  |
| scores.py        | Finds the 'best word' based on manual color weighing                  |
| validAnswers.txt | Words that the wordle answers are drawn from                          |
| validWords.txt   | Words that can be guessed in wordle                                   |
| wordle.py        | Contains useful functions to be used in other files                   |
| words.py         | Basic method for finding the best word using character frequency      |
| newGame.py       | Uses genPossible() from wordle.py to solve games (can solve all games)|

Any other files are likely part of testing, or just for reference.
