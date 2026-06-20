import sys

def merge_sort_count(arr):
    """Return sorted array and inversion count."""
    n = len(arr)
    if n <= 1:
        return arr, 0
    mid = n // 2
    left, inv_left = merge_sort_count(arr[:mid])
    right, inv_right = merge_sort_count(arr[mid:])
    merged = []
    i = j = 0
    inv = inv_left + inv_right
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
            inv += len(left) - i
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged, inv

data = sys.stdin.read().split()
n = int(data[0])
arr = [int(x) for x in data[1:1+n]]
_, ans = merge_sort_count(arr)
print(ans)
