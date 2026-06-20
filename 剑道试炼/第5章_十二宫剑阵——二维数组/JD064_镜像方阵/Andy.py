while True:
 n=int(input())
 if n==0:break
 for i in range(n):
  print(''.join(f'{abs(i-j)+1:3d}'for j in range(n)))
 print()
