import sys
lines = sys.stdin.read().splitlines()
s = lines[0] if len(lines) > 0 else ''
a = lines[1] if len(lines) > 1 else ''
b = lines[2] if len(lines) > 2 else ''
words = s.split()
result = ' '.join(b if w == a else w for w in words)
print(result)
