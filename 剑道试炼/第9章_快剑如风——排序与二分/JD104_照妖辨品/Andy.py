import sys

def quick_select(nums, left, right, k):
    if left == right:
        return nums[left]
    target = nums[left]
    i, j = left - 1, right + 1
    while i < j:
        i += 1
        while nums[i] < target:
            i += 1
        j -= 1
        while nums[j] > target:
            j -= 1
        if i < j:
            nums[i], nums[j] = nums[j], nums[i]
    sl = j - left + 1
    if k <= sl:
        return quick_select(nums, left, j, k)
    else:
        return quick_select(nums, j + 1, right, k - sl)

data = sys.stdin.read().split()
n, k = int(data[0]), int(data[1])
arr = list(map(int, data[2:2 + n]))
print(quick_select(arr, 0, n - 1, k))