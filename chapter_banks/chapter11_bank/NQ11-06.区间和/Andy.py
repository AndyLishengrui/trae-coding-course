# 区间和
n, m = map(int, input().split())
adds = []
queries = []
all_x = []
for _ in range(n):
    x, c = map(int, input().split())
    adds.append((x, c))
    all_x.append(x)
for _ in range(m):
    l, r = map(int, input().split())
    queries.append((l, r))
    all_x.append(l)
    all_x.append(r)
all_x = sorted(set(all_x))
idx = {v: i + 1 for i, v in enumerate(all_x)}
a = [0] * (len(all_x) + 1)
s = [0] * (len(all_x) + 1)
for x, c in adds:
    a[idx[x]] += c
for i in range(1, len(all_x) + 1):
    s[i] = s[i - 1] + a[i]
for l, r in queries:
    print(s[idx[r]] - s[idx[l] - 1])
