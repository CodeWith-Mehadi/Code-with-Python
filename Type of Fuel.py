alcohol_count = 0
gasoline_count = 0
diesel_count = 0

while True:
    fuel_code = int(input())

    if fuel_code == 1:
        alcohol_count += 1
    elif fuel_code == 2:
        gasoline_count += 1
    elif fuel_code == 3:
        diesel_count += 1
    elif fuel_code == 4:
        break
    else:
        continue

print("MUITO OBRIGADO")
print(f"Alcool: {alcohol_count}")
print(f"Gasolina: {gasoline_count}")
print(f"Diesel: {diesel_count}")