# NQ: AcWing 714
x, y = map(int, input().split())
if x > y: x, y = y, x
print(sum(i for i in range(x + 1, y) if i % 2))
