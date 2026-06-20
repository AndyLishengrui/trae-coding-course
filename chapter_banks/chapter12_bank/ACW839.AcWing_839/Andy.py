# 模拟堆
import sys
n = int(input())
h = [0] * 100010
hp = [0] * 100010
ph = [0] * 100010
sz = 0
idx = 0

def heap_swap(a, b):
    ph[hp[a]], ph[hp[b]] = b, a
    hp[a], hp[b] = hp[b], hp[a]
    h[a], h[b] = h[b], h[a]

def down(u):
    t = u
    if u * 2 <= sz and h[u * 2] < h[t]:
        t = u * 2
    if u * 2 + 1 <= sz and h[u * 2 + 1] < h[t]:
        t = u * 2 + 1
    if u != t:
        heap_swap(u, t)
        down(t)

def up(u):
    while u // 2 > 0 and h[u] < h[u // 2]:
        heap_swap(u, u // 2)
        u //= 2

for _ in range(n):
    parts = sys.stdin.readline().split()
    op = parts[0]
    if op == 'I':
        x = int(parts[1])
        sz += 1
        idx += 1
        ph[idx] = sz
        hp[sz] = idx
        h[sz] = x
        up(sz)
    elif op == 'PM':
        print(h[1])
    elif op == 'DM':
        heap_swap(1, sz)
        sz -= 1
        down(1)
    elif op == 'D':
        k = int(parts[1])
        u = ph[k]
        heap_swap(u, sz)
        sz -= 1
        down(u)
        up(u)
    else:
        k, x = int(parts[1]), int(parts[2])
        u = ph[k]
        h[u] = x
        down(u)
        up(u)
