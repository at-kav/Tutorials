# Exercise 7
import random
doubles=0
num_of_times = int(input('Enter the number of times you need to roll the dice : '))
for x in range(num_of_times):
    dice1 = random.randint(1,7)
    dice2 = random.randint(1,7)
    if dice1 == dice2:
        doubles += 1

print('out of',num_of_times,'you rolled',doubles,'doubles')