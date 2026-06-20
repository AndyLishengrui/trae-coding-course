s = float(input())
if s <= 400: p = 15
elif s <= 800: p = 12
elif s <= 1200: p = 10
elif s <= 2000: p = 7
else: p = 4
r = s * p / 100
print(f"New salary: {s + r:.2f}")
print(f"Increase: {r:.2f}")
print(f"Percentage: {p} %")
