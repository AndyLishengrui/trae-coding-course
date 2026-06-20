import sys
data = sys.stdin.read().split()
n = int(data[0])
c = r = f = 0
idx = 1
for _ in range(n):
    k = int(data[idx]); t = data[idx + 1]
    idx += 2
    if t == 'C': c += k
    elif t == 'R': r += k
    else: f += k
s = c + r + f
print(f"Total: {s} weapons")
print(f"Total swords: {c}")
print(f"Total blades: {r}")
print(f"Total spears: {f}")
print(f"Percentage of swords: {c / s * 100:.2f} %")
print(f"Percentage of blades: {r / s * 100:.2f} %")
print(f"Percentage of spears: {f / s * 100:.2f} %")
