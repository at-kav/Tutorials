# Exercise 10

import random

hidden = random.randint(1,20)
guesses_taken = 0
while (guesses_taken <= 5):
    guesses_taken  += 1
    guess=int(input('Enter a guess between 1 and 20:'))
    if guess == hidden:
        break
    elif guess > hidden:
        print('Guess is too high')
    else:
        print('Guess is too low')

if guess==hidden:
    print('you got it in',guesses_taken,'guesses')
else:
    print('Not Guessed.The correct answer was : ',hidden)