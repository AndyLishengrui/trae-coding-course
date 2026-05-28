import sys
data = sys.stdin.read().split()
t = data[0]
s = 0.0
idx = 1
for i in range(12):
    for j in range(12):
        x = float(data[idx]); idx += 1
        if j > i and i + j > 10: s += x
print(f"{s:.1f}" if t == 'S' else f"{s/30:.1f}")
