import sys
data = sys.stdin.read().split()
n = int(data[0])
idx = 1
for _ in range(n):
    p1, p2 = data[idx], data[idx+1]
    idx += 2
    if p1 == p2: print('Tie')
    elif (p1=='Hunter' and p2=='Gun') or (p1=='Bear' and p2=='Hunter') or (p1=='Gun' and p2=='Bear'):
        print('Player1')
    else:
        print('Player2')
