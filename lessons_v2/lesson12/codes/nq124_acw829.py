# 模拟队列
from collections import deque
m = int(input())
q = deque()
for _ in range(m):
    parts = input().split()
    op = parts[0]
    if op == 'push':
        q.append(int(parts[1]))
    elif op == 'pop':
        q.popleft()
    elif op == 'query':
        print(q[0])
    else:
        print('YES' if not q else 'NO')
