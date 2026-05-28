# 表达式求值
s = input().strip()
num = []
op = []
pri = {'+': 1, '-': 1, '*': 2, '/': 2}

def eval_op():
    b = num.pop()
    a = num.pop()
    c = op.pop()
    if c == '+':
        num.append(a + b)
    elif c == '-':
        num.append(a - b)
    elif c == '*':
        num.append(a * b)
    else:
        num.append(int(a / b))

i = 0
while i < len(s):
    c = s[i]
    if c == ' ':
        i += 1
        continue
    if c.isdigit():
        j = i
        while j < len(s) and s[j].isdigit():
            j += 1
        num.append(int(s[i:j]))
        i = j
        continue
    if c == '(':
        op.append(c)
    elif c == ')':
        while op[-1] != '(':
            eval_op()
        op.pop()
    else:
        while op and op[-1] != '(' and pri.get(op[-1], 0) >= pri.get(c, 0):
            eval_op()
        op.append(c)
    i += 1
while op:
    eval_op()
print(num[-1])
