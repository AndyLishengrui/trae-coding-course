prices = {1: 4.0, 2: 4.5, 3: 5.0, 4: 2.0, 5: 1.5}
x, y = map(int, input().split())
print(f"Total: R$ {prices[x] * y:.2f}")
