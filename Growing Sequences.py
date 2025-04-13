while True:
    x = int(input())
    if x == 0:
        break
    sequence = [str(i) for i in range(1, x + 1)]
    print(" ".join(sequence))
