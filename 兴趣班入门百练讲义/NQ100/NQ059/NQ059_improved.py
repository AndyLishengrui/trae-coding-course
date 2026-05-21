def three_sum(nums, target):
    res = []
    n = len(nums)
    nums.sort()
    
    for i in range(n):
        # 跳过重复元素
        if i > 0 and nums[i] == nums[i-1]:
            continue
        
        # 双指针初始化
        j, k = i + 1, n - 1
        while j < k:
            current_sum = nums[i] + nums[j] + nums[k]
            
            if current_sum == target:
                # 满足x<y<z
                if nums[i] < nums[j] and nums[j] < nums[k]:
                    res.append([nums[i], nums[j], nums[k]])
                # 跳重复
                while j < k and nums[j] == nums[j+1]:
                    j += 1
                while j < k and nums[k] == nums[k-1]:
                    k -= 1
                # 移动指针
                j += 1
                k -= 1
            elif current_sum > target:
                k -= 1 # 和过大，右指针左移
            else:
                j += 1 # 和过小，左指针右移
    
    return res

def main():
    import sys
    input = sys.stdin.read().split()
    idx = 0
    target = int(input[idx])
    idx += 1
    n = int(input[idx])
    idx += 1
    nums = list(map(int, input[idx:idx+n]))
    idx += n
    
    result = three_sum(nums, target)
    for triplet in result:
        print('{0} {1} {2}'.format(triplet[0], triplet[1], triplet[2]))

if __name__ == "__main__":
    main()