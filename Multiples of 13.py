X = int(input())
Y = int(input())

start = min(X, Y)
end = max(X, Y)

total = 0

for i in range(start, end + 1):
    if i % 13 != 0:
        total = total + i

print(total)
