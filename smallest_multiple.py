# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

smallestNumberFound = False
number = 20
dividers = range(1, 21)
i = 0

while(not smallestNumberFound):
    if (number % dividers[i] != 0):
        i = 0
        number += 1
        continue
    else:
        i += 1

    if (i == 20):
        smallestNumberFound = True

print(number)