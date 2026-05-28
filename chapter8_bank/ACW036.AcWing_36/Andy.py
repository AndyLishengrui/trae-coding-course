import sys
lines = sys.stdin.read().strip().split('\n')
a = [int(x) for x in lines[0].split() if x != '-1']
b = [int(x) for x in lines[1].split() if x != '-1']
i = j = 0
res = []
while i < len(a) and j < len(b):
    if a[i] <= b[j]: res.append(str(a[i])); i += 1
    else: res.append(str(b[j])); j += 1
res.extend(str(x) for x in a[i:])
res.extend(str(x) for x in b[j:])
print(' '.join(res))
