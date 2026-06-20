import sys
data = sys.stdin.read().split()
l = int(data[0])
t = data[1]
s = 0.0
idx = 2
for i in range(12):
    for j in range(12):
        x = float(data[idx])
        idx += 1
        if i == l:
            s += x
print(f"{s if t == 'S' else s / 12:.1f}")
