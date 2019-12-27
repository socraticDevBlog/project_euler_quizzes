# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
# a2 + b2 = c2

# For example, 32 + 42 = 9 + 16 = 25 = 52.

# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

squares = []
for integer in range(0, 998):
    squares.append(integer ** 2)

for a, squaredA in enumerate(squares):
    for b, squaredB in enumerate(squares):
        for c, squaredC in enumerate(squares):
            if (a+b+c) == 1000:
                if (squaredA+squaredB) == squaredC:
                    print(a*b*c)
