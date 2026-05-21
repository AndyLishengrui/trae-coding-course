def lower_bound(arr, left, right, target):
    """查找第一个不小于target的元素的索引"""
    while left < right:
        mid = left + (right - left) // 2
        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid
    return left

def upper_bound(arr, left, right, target):
    """查找第一个大于target的元素的索引"""
    while left < right:
        mid = left + (right - left) // 2
        if arr[mid] <= target:
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
    
    g = [-1000000000] * (n + 2)
    for i in range(1, n+1):
        g[i] = int(input[idx])
        idx += 1
    g[n+1] = 1000000000
    
    m = int(input[idx])
    idx += 1
    
    for _ in range(m):
        t = int(input[idx])
        idx += 1
        
        l = lower_bound(g, 1, n+1, t)
        r = upper_bound(g, 1, n+1, t)
        if l <= n:
            l -= 1
        
        if l == n + 1:
            print(g[n])
        elif r == 1:
            print(g[1])
        else:
            if t - g[l] > g[r] - t:
                print(g[r])
            else:
                print(g[l])

if __name__ == "__main__":
    main()