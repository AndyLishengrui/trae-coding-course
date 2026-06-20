import sys
data = sys.stdin.read().split()
t = data[0]
s = 0.0
idx = 1
for i in range(12):
    for j in range(12):
        x = float(data[idx])
        idx += 1
        if j > i:
            s += x
print(f"{s if t == 'S' else s / 66:.1f}")
