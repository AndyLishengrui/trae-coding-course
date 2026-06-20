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
print(f"Total: {s} animals")
print(f"Total coneys: {c}")
print(f"Total rats: {r}")
print(f"Total frogs: {f}")
print(f"Percentage of coneys: {c / s * 100:.2f} %")
print(f"Percentage of rats: {r / s * 100:.2f} %")
print(f"Percentage of frogs: {f / s * 100:.2f} %")
