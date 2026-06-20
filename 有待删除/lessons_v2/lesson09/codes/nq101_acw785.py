# 快速排序
def quicksort(arr, l, r):
    if l >= r:
        return
    x = arr[(l + r) // 2]
    i, j = l - 1, r + 1
    while i < j:
        i += 1
        while arr[i] < x:
            i += 1
        j -= 1
        while arr[j] > x:
            j -= 1
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
    quicksort(arr, l, j)
    quicksort(arr, j + 1, r)

n = int(input())
arr = list(map(int, input().split()))
quicksort(arr, 0, n - 1)
print(' '.join(map(str, arr)))
