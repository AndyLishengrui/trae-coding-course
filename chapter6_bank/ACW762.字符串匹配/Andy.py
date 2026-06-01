import sys
lines = sys.stdin.read().splitlines()
a = lines[0] if len(lines) > 0 else ''
b = lines[1] if len(lines) > 1 else ''
print("yes" if b in a else "no")
