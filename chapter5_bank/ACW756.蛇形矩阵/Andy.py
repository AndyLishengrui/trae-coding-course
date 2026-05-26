n,m=map(int,input().split());a=[[0]*m for _ in range(n)]
dx=[0,1,0,-1];dy=[1,0,-1,0];d=0;x=y=0
for v in range(1,n*m+1):
 a[x][y]=v;nx=x+dx[d];ny=y+dy[d]
 if nx<0 or nx>=n or ny<0 or ny>=m or a[nx][ny]:d=(d+1)%4;nx=x+dx[d];ny=y+dy[d]
 x,y=nx,ny
for r in a:print(' '.join(map(str,r)))
