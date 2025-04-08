N = int(input())

total = 0
coelho = 0
rato = 0
sapo = 0

for _ in range(N):
    amount, type_animal = input().split()
    amount = int(amount)
    total = total + amount

    if type_animal == 'C':
        coelho = coelho + amount
    elif type_animal == 'R':
        rato = rato + amount
    elif type_animal == 'S':
        sapo = sapo + amount

perc_coelho = (coelho / total) * 100
perc_rato = (rato / total) * 100
perc_sapo = (sapo / total) * 100

print(f"Total: {total} cobaias")
print(f"Total de coelhos: {coelho}")
print(f"Total de ratos: {rato}")
print(f"Total de sapos: {sapo}")
print(f"Percentual de coelhos: {perc_coelho:.2f} %")
print(f"Percentual de ratos: {perc_rato:.2f} %")
print(f"Percentual de sapos: {perc_sapo:.2f} %")
