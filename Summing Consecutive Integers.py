values = list(map(int, input().split()))

a = values[0]
n = 0

for val in values[1:]:
    if val > 0:
        n = val
        break

total = sum(a + i for i in range(n))
print(total)
