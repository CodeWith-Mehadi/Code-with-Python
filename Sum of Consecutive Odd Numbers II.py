N = int(input())

for _ in range(N):
    X, Y = map(int, input().split())

    if X > Y:
        X, Y = Y, X

    total = 0
    for i in range(X + 1, Y):
        if i % 2 == 1:
            total = total + i

    print(total)
