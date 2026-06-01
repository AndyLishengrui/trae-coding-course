import sys
data = sys.stdin.read().split()
if data:
    x = float(data[0])
    y = float(data[1])
    print(f"{x / y:.3f} km/l")
