count = 0

for read in range(6):
    number = float(input())

    if number >= 0:
        count = count + 1
print(f"{count} valores positivos")