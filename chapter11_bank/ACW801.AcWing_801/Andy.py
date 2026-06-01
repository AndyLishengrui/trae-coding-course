import sys
data = sys.stdin.read().split()
n = int(data[0])
out = []
for i in range(1, n + 1):
    out.append(str(bin(int(data[i])).count('1')))
sys.stdout.write(' '.join(out) + ' ')
