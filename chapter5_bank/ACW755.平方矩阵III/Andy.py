while True:
 n=int(input())
 if n==0:break
 w=len(str(2**(2*n-2)))+1
 for i in range(n):
  print(''.join(f'{2**(i+j):{w}d}'for j in range(n)))
 print()
