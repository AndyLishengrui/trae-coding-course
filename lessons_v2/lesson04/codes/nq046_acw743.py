# NQ: AcWing 743
r = int(input())
t = input().strip()
m = [list(map(float, input().split())) for _ in range(12)]
s = sum(m[r])
print(f"{s:.1f}" if t == 'S' else f"{s / 12:.1f}")
