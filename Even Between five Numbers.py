count = 0

for _ in range(5) :
    number = int(input())
    if number % 2 == 0 :
        count = count + 1
print(f"{count} valores pares")