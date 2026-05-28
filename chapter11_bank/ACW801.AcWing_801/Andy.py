import sys
n = int(sys.stdin.read().split()[0])
print(bin(n).count('1'))
