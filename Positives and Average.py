count = 0
total = 0

for _ in range(6) :
    number = float(input())
    if number > 0 :
        count = count + 1
        total = total + number
print(f"{count} valores positivos")
print(f"{total / count:.1f}")