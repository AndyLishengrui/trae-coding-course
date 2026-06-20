import sys
data = sys.stdin.read().split()
if data:
    n = int(data[0])
    h = int(data[1])
    m = float(data[2])
    print(f"NUMBER = {n}")
    print(f"SALARY = U$ {h * m:.2f}")
