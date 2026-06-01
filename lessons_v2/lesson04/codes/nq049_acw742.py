import sys
data = sys.stdin.read().split()
n = int(data[0])
a = list(map(int, data[1:1+n]))
mn = min(a)
pos = a.index(mn)
print(f"Menor valor: {mn}")
print(f"Posicao: {pos}")
