amount = float(input())

total_cents = int(round(amount * 100))

print("NOTAS:")
for note in [100, 50, 20, 10, 5, 2]:
    note_count = total_cents // (note * 100)
    print(f"{note_count} nota(s) de R$ {note:.2f}")
    total_cents = total_cents % (note * 100)

print("MOEDAS:")
for coin in [100, 50, 25, 10, 5, 1]:
    coin_count = total_cents // coin
    print(f"{coin_count} moeda(s) de R$ {coin/100:.2f}")
    total_cents = total_cents % coin
