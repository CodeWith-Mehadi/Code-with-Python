pi = 3.14159
A, B, C = map(float, input().split())

area = (1/2) * A * C
radius = pi * (C ** 2)
trapezium =((A+B)/2) * C
square = B ** 2
rectangle = A * B

print(f"TRIANGULO: {area:.3f}")
print(f"CIRCULO: {radius:.3f}")
print(f"TRAPEZIO: {trapezium:.3f}")
print(f"QUADRADO: {square:.3f}")
print(f"RETANGULO: {rectangle:.3f}")