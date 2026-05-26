# NQ: AcWing 744
c = int(input())
t = input().strip()
m = [list(map(float, input().split())) for _ in range(12)]
s = sum(m[i][c] for i in range(12))
print(f"{s:.1f}" if t == 'S' else f"{s / 12:.1f}")
