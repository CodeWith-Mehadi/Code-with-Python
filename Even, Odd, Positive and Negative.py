even = odd = positive = negative = 0

for _ in range(5):
    num = int(input())

    if num % 2 == 0:
        even = even + 1
    else:
        odd = odd + 1

    if num > 0:
        positive = positive + 1
    elif num < 0:
        negative = negative + 1

print(f"{even} valor(es) par(es)")
print(f"{odd} valor(es) impar(es)")
print(f"{positive} valor(es) positivo(s)")
print(f"{negative} valor(es) negativo(s)")
