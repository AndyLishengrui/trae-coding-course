t=input().strip()
q=[list(map(float,input().split())) for _ in range(12)]
s=0
c=0
for i in range(1,12):
    for j in range(12-i,12):
        s+=q[i][j]
        c+=1
if t=='S':
    print('{0:.1f}'.format(s))
else:
    print('{0:.1f}'.format(s/c))