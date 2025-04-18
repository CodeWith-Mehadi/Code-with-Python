N = int(input())
for _ in range(N):
    X, Y = map(int, input().split())

    if X % 2 == 0:
        X = X + 1

    total = 0
    count = 0
    current = X

    while count < Y:
        total = total + current
        current = current + 2
        count = count + 1

    print(total)