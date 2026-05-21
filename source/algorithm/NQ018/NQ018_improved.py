# NQ018 计算折线长度
import math
n=int(input())
for _ in range(n):
    x1,y1,x2,y2=map(int,input().split())
    if x1+y1>x2+y2:x1,x2=x2,x1;y1,y2=y2,y1
    S2=x2+y2
    len=0.0
    sqrt2=math.sqrt(2.0)
    while x1!=x2 or y1!=y2:
        S1=x1+y1
        if y1==0:
            len+=math.sqrt(1.0*S1*S1+1.0*(S1+1)*(S1+1))
            x1=0;y1=S1+1
        else:
            steps=y1 if S1<S2 else x2-x1
            len+=steps*sqrt2
            x1+=steps;y1-=steps
    print('{0:.3f}'.format(len))