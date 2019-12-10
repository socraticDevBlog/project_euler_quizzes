#Find the sum of all the multiples of 3 or 5 below 1000.

def isMultipleOf3or5(input):
    return (input%3==0) or (input%5==0)

result = 0

for x in range(1000):
    if (isMultipleOf3or5(x)):
        result += x

print(result)
