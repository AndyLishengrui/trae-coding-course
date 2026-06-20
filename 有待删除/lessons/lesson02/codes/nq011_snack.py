# NQ011: 零食
# 用dict做映射表 — Pythonic风格
prices = {1: 4.0, 2: 4.5, 3: 5.0, 4: 2.0, 5: 1.5}
code, qty = map(int, input().split())
total = prices[code] * qty
print(f"Total: R$ {total:.2f}")
