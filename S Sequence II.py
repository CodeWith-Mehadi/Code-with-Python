S = 0.0
for i in range(0, 20) :
    numerator = 2 * i + 1
    denominator = 2 ** i
    S = S + numerator / denominator
print(f"{S:.2f}")