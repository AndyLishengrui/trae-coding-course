import math

def calculate(n, m):
    res = 0.0
    a = float(n)
    for _ in range(m):
        res += a
        a = math.sqrt(a)
    return res

inputs = [
    (65004, 5750),
    (87184, 2112),
    (94597, 561),
    (80010, 2732),
    (58744, 7710)
]

print("Python double precision results:")
for n, m in inputs:
    print(f"{n} {m} -> {calculate(n, m):.2f}")
