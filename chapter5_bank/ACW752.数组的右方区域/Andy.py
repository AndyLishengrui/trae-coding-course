t=input().strip();s=c=0
for i in range(12):
 for j in range(12):
  x=float(input())
  if j>i and i+j>10:s+=x;c+=1
print(f'{s if t=="S" else s/c:.1f}')
