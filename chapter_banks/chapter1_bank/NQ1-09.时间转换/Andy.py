import sys
data = sys.stdin.read().split()
if data:
    n = int(data[0])
    h = n // 3600
    m = n % 3600 // 60
    s = n % 60
    print(f"{h}:{m}:{s}")
