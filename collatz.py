largest=0
start=0
i=1000000
current=0
counter=0

while i <= 1000000:
    current = i
    counter = 0
    while current !=1:
        if current % 2 == 0:
            current = current / 2
        else:
            current = 3 * current + 1

        counter = counter + 1

    if counter > largest:
        largest = counter
        start = i

    i = i-1

print(start)