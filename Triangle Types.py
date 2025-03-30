A, B, C = map(float, input().split())

side = sorted([A, B, C], reverse=True)
A, B, C = side[0], side[1], side[2]

if A >= B + C:
    print("NAO FORMA TRIANGULO")
else:
    if A ** 2 == (B ** 2) + (C ** 2):
        print("TRIANGULO RETANGULO")
    if A ** 2 > (B ** 2) + (C ** 2):
        print("TRIANGULO OBTUSANGULO")
    if A ** 2 < (B ** 2) + (C ** 2):
        print("TRIANGULO ACUTANGULO")

    if A == B == C:
        print("TRIANGULO EQUILATERO")
    elif A == B or B == C or C == A:
        print("TRIANGULO ISOSCELES")