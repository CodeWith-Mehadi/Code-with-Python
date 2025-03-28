product_code, quantity = map(int, input().split())

if product_code == 1:
    price = 4.00
elif product_code == 2:
    price = 4.50
elif product_code == 3:
    price = 5.00
elif product_code == 4:
    price = 2.00
elif product_code == 5:
    price = 1.50

total = price * quantity
print(f"Total: R$ {total:.2f}")