import sys
s = sys.stdin.read().rstrip('\n')
n = len(s)
result = ''.join(chr(ord(s[i]) + ord(s[(i+1) % n])) for i in range(n))
print(result)
