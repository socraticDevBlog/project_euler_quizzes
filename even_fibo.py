#even fibonacci

sum = 2 #because previous1 is an even integer !
previous1 = 2
previous2 = 1
actual = 3

while actual < 4000000:
    
    if (actual%2==0):
        sum += actual

    previous2 = previous1
    previous1 = actual
    actual = previous1 + previous2

print(sum)