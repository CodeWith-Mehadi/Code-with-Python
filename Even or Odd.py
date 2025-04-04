N = int(input())

for i in range(N):
    x = int(input())

    if x == 0:
        print("NULL")
    else:
        if x % 2 == 0:
            type1 = "EVEN"
        else:
            type1 = "ODD"

        if x > 0:
            type2 = "POSITIVE"
        else:
            type2 = "NEGATIVE"

        print(type1, type2)
