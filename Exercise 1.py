# Exercise 1

import random

hidden = random.randint(1,20)
guess = None
while (guess != hidden):
    guess=int(input('Enter a guess between 1 and 20:'))
    if guess != hidden:
        print(guess,'is not correct')
    else:
        print(guess,'was correct')
    if guess >= hidden:
        print('Guess is too high')
    else:
        print('Guess is too low')