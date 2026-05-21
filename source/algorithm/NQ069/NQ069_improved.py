def lower_bound(arr, left, right, target):
    """查找第一个不小于target的元素的索引"""
    while left < right:
        mid = left + (right - left) // 2
        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid
    return left

def main():
    import sys
    input = sys.stdin.read().split()
    idx = 0
    
    n = int(input[idx])
    idx += 1
    
    nums = list(map(int, input[idx:idx+n]))
    idx += n
    
    target = int(input[idx])
    idx += 1
    
    nums.sort()
    
    for i in range(n):
        complement = target - nums[i]
        left = i + 1
        right = n
        pos = lower_bound(nums, left, right, complement)
        
        if pos < n and nums[pos] == complement:
            print(nums[i], complement)
            return
    
    print('No')

if __name__ == "__main__":
    main()