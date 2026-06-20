import sys
for line in sys.stdin:
    s = line.rstrip('\n')
    if not s:
        continue
    res = []
    for c in s:
        if c == ' ':
            res.append('%20')
        else:
            res.append(c)
    print(''.join(res))
