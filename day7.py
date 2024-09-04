import nltk
#nltk.download('words')
import random
from nltk.corpus import words
import time
import sys
status = True
word_list = words.words()
random_word = random.choice(word_list)
guess = ''
newlist = []
lives = 6
s = list(random_word)
def blank(word):
    print(word)
    for i in range(len(word)):
        newlist.append('_')
    print(list)
def substitute(word,guess):
    for i in s:
        if guess == i:
            newlist[word.index(i)] = i
            s[word.index(i)] ='_'
        else:
            continue
    listToStr = ''.join(map(str, newlist))
    print(listToStr)
    return listToStr
def guess(word,guess):
    if guess in word:
        result = substitute(s,guess)
        return result
    else:
        return False
def Hangeman(lives):
    cases = ["""
        ------
        |    |
        |
        |
        |
        |
        |
    ------------
    """, """
        ------
        |    |
        |    O
        |
        |
        |
        |
    ------------
    """, """
        ------
        |    |
        |    O
        |    |
        |    |
        |
        |
    ------------
    """, """
        ------
        |    |
        |    O
        |    |
        |    |
        |   /
        |
    ------------
    """, """
        ------
        |    |
        |    O
        |    |
        |    |
        |   / \\
        |
    ------------
    """, """
        ------
        |    |
        |    O
        |  --|
        |    |
        |   / \\
        |
    ------------
    """, """
        ------
        |    |
        |    O
        |  --|--
        |    |
        |   / \\
        |
    ------------
    """]
    if lives == 6:
        return cases[0]
    elif lives == 5:
        return cases[1]
    elif lives == 4:
        return cases[2]
    elif lives == 3:
        return cases[3]
    elif lives == 2:
        return cases[4]
    elif lives == 1:
        return cases[5]
    elif lives == 0:
        return cases[6]
blank(random_word)
while status == True:
    user_guess = str(input('what is your guess?'))
    wg = guess(random_word,user_guess)
    if wg == False:
        lives = lives - 1
    print(Hangeman(lives))
    if lives == 0:
        print('Gameover')
        break
    if wg == random_word:
        print('You won!')
        time.sleep(5)
        sys.exit()