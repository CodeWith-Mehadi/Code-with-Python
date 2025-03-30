a, b, c = map(int, input().split())

original_value = [a, b, c]
sorted_value = sorted (original_value)

for value in sorted_value :
    print(value)

print()

for value in original_value :
    print(value)