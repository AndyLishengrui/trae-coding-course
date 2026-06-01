import sys
data = sys.stdin.read().split()
p1, p2 = data[0], data[1]
if p1 == p2: print('Tie')
elif (p1=='Hunter' and p2=='Gun') or (p1=='Bear' and p2=='Hunter') or (p1=='Gun' and p2=='Bear'):
    print('Player1')
else:
    print('Player2')
