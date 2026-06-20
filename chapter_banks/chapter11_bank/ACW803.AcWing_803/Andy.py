import sys
data = sys.stdin.read().split()
n = int(data[0])
segs = []
idx = 1
for _ in range(n):
    l, r = int(data[idx]), int(data[idx+1])
    idx += 2
    segs.append((l, r))
segs.sort()
merged = []
st, ed = segs[0]
for l, r in segs[1:]:
    if l <= ed: ed = max(ed, r)
    else: merged.append((st, ed)); st, ed = l, r
merged.append((st, ed))
print(len(merged))
for l, r in merged: print(l, r)
