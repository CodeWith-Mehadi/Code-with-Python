i = 0.0

while i <= 2.0:
    for j in range(1, 4):
        I = round(i, 1)
        J = round(i + j, 1)

        if I == int(I):
            I = int(I)
        if J == int(J):
            J = int(J)

        print(f"I={I} J={J}")

    i = i + 0.2
