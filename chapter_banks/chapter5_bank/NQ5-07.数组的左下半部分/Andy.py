t=input().strip();s=0
for i in range(12):
 for j in range(12):
  x=float(input())
  if j<i:s+=x
print(f'{s if t=="S" else s/66:.1f}')
