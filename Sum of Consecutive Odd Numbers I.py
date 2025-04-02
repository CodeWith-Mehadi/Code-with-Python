X = int(input())
Y = int(input())

if X > Y :
    X, Y = Y, X
os = 0
for i in range(X + 1, Y) :
    if i % 2 != 0 :
        os = os + i
print(os)
