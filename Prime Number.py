import math

N = int(input())
for _ in range(N):
    X = int(input())
    if X <= 1:
        print(f"{X} nao eh primo")
    else:
        is_prime = True
        for i in range(2, int(math.sqrt(X)) + 1):
            if X % i == 0:
                is_prime = False
                break
        if is_prime:
            print(f"{X} eh primo")
        else:
            print(f"{X} nao eh primo")
