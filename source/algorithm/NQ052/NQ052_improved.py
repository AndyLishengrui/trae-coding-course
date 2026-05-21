import sys

def quick_sort(nums, left, right):
    if left >= right:
        return
    pivot = nums[left]
    i, j = left - 1, right + 1
    while i < j:
        i += 1
        while nums[i] < pivot:
            i += 1
        j -= 1
        while nums[j] > pivot:
            j -= 1
        if i < j:
            nums[i], nums[j] = nums[j], nums[i]
    quick_sort(nums, left, j)
    quick_sort(nums, j + 1, right)

def main():
    input = sys.stdin.read().split()
    n = int(input[0])
    nums = list(map(int, input[1:n+1]))
    quick_sort(nums, 0, n - 1)
    print(' '.join(map(str, nums)))

if __name__ == "__main__":
    main()