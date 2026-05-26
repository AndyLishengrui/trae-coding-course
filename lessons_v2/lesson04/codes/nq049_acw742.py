# NQ: AcWing 742
n = int(input())
arr = list(map(int, input().split()))
mn = min(arr)
print(f"Menor valor: {mn}")
print(f"Posicao: {arr.index(mn)}")
