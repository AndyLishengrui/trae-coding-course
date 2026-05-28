import sys

stack1 = []
stack2 = []

for line in sys.stdin:
    line = line.strip()
    if not line:
        continue
    parts = line.split()
    if parts[0] == 'push':
        stack1.append(int(parts[1]))
    elif parts[0] == 'pop':
        if not stack2:
            while stack1:
                stack2.append(stack1.pop())
        if stack2:
            print(stack2.pop())
    elif parts[0] == 'peek':
        if not stack2:
            while stack1:
                stack2.append(stack1.pop())
        if stack2:
            print(stack2[-1])
    elif parts[0] == 'empty':
        print('true' if (not stack1 and not stack2) else 'false')
