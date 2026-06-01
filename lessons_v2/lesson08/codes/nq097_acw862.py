n = int(input())
data = []
for _ in range(n):
    parts = input().split()
    x = int(parts[0])
    y = float(parts[1])
    z = parts[2]
    data.append((x, y, z))
data.sort(key=lambda t: t[0])
for x, y, z in data:
    print(f'{x} {y:.2f} {z}')
