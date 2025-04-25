T = int(input())
N = []

for i in range(1000):
    value = i % T
    N.append(value)

for i in range(1000):
    print(f"N[{i}] = {N[i]}")