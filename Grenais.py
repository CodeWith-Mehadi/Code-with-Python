inter_wins = 0
gremio_wins = 0
draws = 0
total_matches = 0

while True:
    inter, gremio = map(int, input().split())
    total_matches = total_matches + 1

    if inter > gremio:
        inter_wins = inter_wins + 1
    elif gremio > inter:
        gremio_wins = gremio_wins + 1
    else:
        draws = draws + 1

    print("Novo grenal (1-sim 2-nao)")
    choice = int(input())
    while choice not in [1, 2]:
        print("Novo grenal (1-sim 2-nao)")
        choice = int(input())

    if choice == 2:
        break

print(f"{total_matches} grenais")
print(f"Inter:{inter_wins}")
print(f"Gremio:{gremio_wins}")
print(f"Empates:{draws}")

if inter_wins > gremio_wins:
    print("Inter venceu mais")
elif gremio_wins > inter_wins:
    print("Gremio venceu mais")
else:
    print("Não houve vencedor")
