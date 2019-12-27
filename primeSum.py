# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all the primes below two million.

from arithmetics_utils import isPrime

# list of odd numbers
#
primes = range(1, 2000001, 2)

# 2 is the only even prime number
#
accumulator = 2

for integer in primes:
    if isPrime(integer):
        accumulator += integer

print(accumulator)
