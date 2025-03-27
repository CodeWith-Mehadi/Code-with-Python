spent_time = int(input())
average_speed = int(input())

distance = spent_time * average_speed
fuel_needed = distance/12

print(f"{fuel_needed:.3f}")