# NQ010X 数组的右上半部分
t = input().strip()
a = []
for _ in range(12):
    row = list(map(float, input().split()))
    a.append(row)
s = 0
cnt = 0
for i in range(12):
    for j in range(i+1, 12):
        s += a[i][j]
        cnt += 1
if t == 'S':
    print(f"{s:.1f}")
else:
    print(f"{s/cnt:.1f}")