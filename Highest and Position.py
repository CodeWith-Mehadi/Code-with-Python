max_value = -1
position = 0

for i in range(1, 101):
    num = int(input())
    if num > max_value:
        max_value = num
        position = i

print(max_value)
print(position)
