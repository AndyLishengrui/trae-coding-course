while True:
 n=int(input())
 if n==0:break
 for i in range(n):
  row=[]
  for j in range(n):
   v=min(i,j,n-1-i,n-1-j)+1
   row.append(f'{v:3d}')
  print(''.join(row))
 print()
