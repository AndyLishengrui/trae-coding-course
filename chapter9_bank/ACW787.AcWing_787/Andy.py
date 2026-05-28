# 归并排序
def merge_sort(arr, l, r):
    if l >= r:
        return
    mid = (l + r) // 2
    merge_sort(arr, l, mid)
    merge_sort(arr, mid + 1, r)
    tmp = []
    i, j = l, mid + 1
    while i <= mid and j <= r:
        if arr[i] <= arr[j]:
            tmp.append(arr[i])
            i += 1
        else:
            tmp.append(arr[j])
            j += 1
    tmp.extend(arr[i:mid + 1])
    tmp.extend(arr[j:r + 1])
    arr[l:r + 1] = tmp

n = int(input())
arr = list(map(int, input().split()))
merge_sort(arr, 0, n - 1)
print(' '.join(map(str, arr)))
