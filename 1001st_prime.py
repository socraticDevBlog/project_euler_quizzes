# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

# What is the 10 001st prime number?

from arithmetics_utils import isPrime

primes = []

for x in range(150000):
    if isPrime(x):
        primes.append(x)

print(primes[10000])