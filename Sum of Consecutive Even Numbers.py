while True:
    X = int(input())

    if X == 0:
        break
    if X % 2 != 0:
        X = X + 1

    total = 0

    for i in range(5):
        total = total + X + (i * 2)
    print(total)