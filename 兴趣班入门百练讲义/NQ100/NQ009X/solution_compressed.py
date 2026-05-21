# NQ009X 数组中的行
l = int(input())
t = input().strip()
a = []
for _ in range(12):
    row = list(map(float, input().split()))
    a.append(row)
s = sum(a[l])
if t == 'S':
    print(f"{s:.1f}")
else:
    print(f"{s/12:.1f}")