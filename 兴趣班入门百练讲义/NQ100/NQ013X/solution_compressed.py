# NQ013X 数组中的列
c = int(input())
t = input().strip()
a = []
for _ in range(12):
    row = list(map(float, input().split()))
    a.append(row)
s = 0
for i in range(12):
    s += a[i][c]
if t == 'S':
    print(f"{s:.1f}")
else:
    print(f"{s/12:.1f}")