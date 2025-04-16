total_age = 0
count = 0

while True:
    age = int(input())
    if age < 0:
        break
    total_age = total_age + age
    count = count + 1

if count > 0:
    average = total_age / count
    print(f"{average:.2f}")
else:
    print("No valid ages were entered.")
