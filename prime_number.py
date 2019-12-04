# What is the largest prime factor of the number 600851475143 ?

from arithmetics_utils import factors, isPrime

highestPrimeNumber = 1

for x in factors(600851475143):
    if(isPrime(x)):
        if (x > highestPrimeNumber):
            highestPrimeNumber = x    

print(highestPrimeNumber)