N = int(input())
for _ in range(N):
    X = int(input())
    sum = 0
    for i in range(1, X):
        if X % i == 0:
            sum = sum + i
    if sum == X:
        print(f"{X} eh perfeito")
    else:
        print(f"{X} nao eh perfeito")
