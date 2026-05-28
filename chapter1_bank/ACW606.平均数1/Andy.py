import sys
data = sys.stdin.read().split()
if data:
    a = float(data[0])
    b = float(data[1])
    print(f"MEDIA = {(a * 3.5 + b * 7.5) / 11:.5f}")
