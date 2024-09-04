# enemies = 15

# def enemy():
#     enemies = 16
#     print('enemies are:',enemies)

# enemy()
# print('now enemies are:',enemies)
###########################Global################
# enemies = 15

# def enemy():
#     global enemies
#     enemies = 17
#     print('enemies are:',enemies)

# enemy()
# print('now enemies are:',enemies)
#################################Global Constants
# URL = 'http:/jjjjj'

# def con():
#     print(URL)
# con()
############################################
import random
attempts_hard = 5
attempts_easy = 10
NUMBER = random.randint(0,101)
print(NUMBER)
def hard_mode():
    global attempts_hard
    while True:
        if attempts_hard == 0:
            print("LOSERRR")
            return False
        first_str = f"you have {attempts_hard} attempts remaining to guess the number"
        print(first_str)
        print('make a guess')
        num = int(input())
        if num > NUMBER:
            print('too high')
            attempts_hard -= 1
        elif num < NUMBER:
            print('too low')
            attempts_hard -= 1
        elif num == NUMBER:
            print('YEAH CORRECT!')
            return False

def easy_mode():
    global attempts_easy
    while True:
        if attempts_easy == 0:
            print("LOSERRR")
            return False
        first_str = f"you have {attempts_easy} attempts remaining to guess the number"
        print(first_str)
        print('make a guess')
        num = int(input())
        if num > NUMBER:
            print('too high')
            attempts_easy -= 1
        elif num < NUMBER:
            print('too low')
            attempts_easy -= 1
        elif num == NUMBER:
            print('YEAH CORRECT!')
            return False
while True:
    first_str = """Welcome to the Number Guessing Game!
    I'm thinking of a number between 1 and 100.
    Choose a difficulty. Type 'easy' or 'hard':"""

    print(first_str)
    mode = str(input())

    if mode == 'hard':
        if hard_mode() == False:
            break
    elif mode == 'easy':
        if easy_mode() == False:
            break
    else:
        print('invalid input')