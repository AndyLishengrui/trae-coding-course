import sys
data = sys.stdin.read().split()
if data:
    r = float(data[0])
    v = (4.0 / 3.0) * 3.14159 * r ** 3
    print(f"VOLUME = {v:.3f}")
