import sys
import math
data = sys.stdin.read().split()
if data:
    x1, y1, x2, y2 = map(float, data[:4])
    d = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
    print(f"{d:.4f}")
