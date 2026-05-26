# NQ: AcWing 716
n = int(input())
arr = list(map(int, input().split()))[:n]
mx = max(arr)
print(mx)
print(arr.index(mx) + 1)
