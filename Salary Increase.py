salary = float(input())

if salary <= 400.00:
    rate = 0.15
elif salary <= 800.00:
    rate = 0.12
elif salary <= 1200.00:
    rate = 0.10
elif salary <= 2000.00:
    rate = 0.07
else:
    rate = 0.04

earned = salary * rate
new_salary = salary + earned
percentage = int(rate * 100)

print(f"Novo salario: {new_salary:.2f}")
print(f"Reajuste ganho: {earned:.2f}")
print(f"Em percentual: {percentage} %")
