import sys

data = sys.stdin.read().split()
m = int(data[0])
idx_ptr = 1

# Initialize
N = 100010
e = [0] * N
ne = [0] * N
head = -1
idx = 0

for _ in range(m):
    op = data[idx_ptr]
    idx_ptr += 1
    if op == 'H':
        x = int(data[idx_ptr])
        idx_ptr += 1
        e[idx] = x
        ne[idx] = head
        head = idx
        idx += 1
    elif op == 'D':
        k = int(data[idx_ptr])
        idx_ptr += 1
        if k == 0:
            head = ne[head]
        else:
            ne[k - 1] = ne[ne[k - 1]]
    elif op == 'I':
        k = int(data[idx_ptr])
        x = int(data[idx_ptr + 1])
        idx_ptr += 2
        e[idx] = x
        ne[idx] = ne[k - 1]
        ne[k - 1] = idx
        idx += 1

# Output
out = []
i = head
while i != -1:
    out.append(str(e[i]))
    i = ne[i]
print(' '.join(out))