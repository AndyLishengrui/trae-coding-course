a, b, c, d = map(int, input().split())
s = a * 60 + b
e = c * 60 + d
if e <= s: e += 24 * 60
d = e - s
print(f"{d // 60}:{d % 60}")
