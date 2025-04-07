while True:
    X, Y = map(int, input().split())

    if X == 0 or Y == 0:
        break

    if X > 0 and Y > 0:
        print("Q1")
    if X < 0 and Y > 0:
        print("Q2")
    if X < 0 and Y < 0:
        print("Q3")
    if X > 0 and Y < 0:
        print("Q4")