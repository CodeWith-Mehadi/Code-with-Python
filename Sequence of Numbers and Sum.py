while True:
    M, N = map(int, input().split())

    if M <= 0 or N <= 0 :
        break

    small = min(M, N)
    large = max(M, N)

    total = 0
    line = ""

    for i in range(small, large + 1):
        line = line + f"{i} "
        total = total + i

    print(f"{line}Sum={total}")