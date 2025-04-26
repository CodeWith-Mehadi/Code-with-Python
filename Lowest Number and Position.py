N = int(input())

X = list(map(int, input().split()))

smallest = min(X)
position = X.index(smallest)

print(f"Menor valor: {smallest}")
print(f"Posicao: {position}")
