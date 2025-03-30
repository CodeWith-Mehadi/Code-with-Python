a, b = map(int, input().split())

if a < b:
    duration = b - a
else:
    duration = (24 - a) + b

print(f"O JOGO DUROU {duration} HORA(S)")