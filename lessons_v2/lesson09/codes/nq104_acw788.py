import sys
sys.setrecursionlimit(200000)
def merge(a, l, r):
    if l >= r: return 0
    m = (l+r)//2
    cnt = merge(a,l,m) + merge(a,m+1,r)
    tmp = []
    i, j = l, m+1
    while i <= m and j <= r:
        if a[i] <= a[j]: tmp.append(a[i]); i += 1
        else: tmp.append(a[j]); j += 1; cnt += m - i + 1
    tmp.extend(a[i:m+1]); tmp.extend(a[j:r+1])
    a[l:r+1] = tmp
    return cnt
data = sys.stdin.read().split()
n = int(data[0])
arr = list(map(int, data[1:1+n]))
print(merge(arr, 0, n-1))
