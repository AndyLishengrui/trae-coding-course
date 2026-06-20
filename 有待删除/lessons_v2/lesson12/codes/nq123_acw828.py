# 模拟栈
m = int(input())
stk = []
for _ in range(m):
    parts = input().split()
    op = parts[0]
    if op == 'push':
        stk.append(int(parts[1]))
    elif op == 'pop':
        stk.pop()
    elif op == 'query':
        print(stk[-1])
    else:
        print('YES' if not stk else 'NO')
