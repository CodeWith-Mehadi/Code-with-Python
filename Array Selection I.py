A = []
for i in range(100):
    num = float(input())
    A.append(num)

for i in range(100):
    if A[i] <= 10:
        print(f"A[{i}] = {A[i]:.1f}")
