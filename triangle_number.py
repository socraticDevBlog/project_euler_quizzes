# What is the value of the first triangle number to have over five hundred divisors?

# https://projecteuler.net/problem=12

from arithmetics_utils import returnTriangleNumberByBase, factors

global_divisors = []
triangle_number = 0
base_size = 0

while (len(global_divisors) < 500):
    base_size += 1
    triangle_number = returnTriangleNumberByBase(base_size)
    global_divisors = factors(triangle_number)

print(triangle_number)