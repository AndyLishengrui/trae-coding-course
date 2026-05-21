def four_sum(nums, target):
    """找到所有满足四数之和等于目标值的四元组"""
    res = []         # 答案数组
    nums.sort()      # 排序
    
    n = len(nums)
    
    # 四重循环，后两重用双指针算法 i,j,k,l
    for i in range(n):
        # 去重
        if i > 0 and nums[i] == nums[i-1]:
            continue
        
        for j in range(i + 1, n):
            # 去重
            if j > i + 1 and nums[j] == nums[j-1]:
                continue
            
            # 双指针算法
            l = n - 1
            for k in range(j + 1, n):
                # 去重
                if k > j + 1 and nums[k] == nums[k-1]:
                    continue
                
                # 找到最小的l使得四数之和大于等于目标值
                while k < l - 1 and nums[i] + nums[j] + nums[k] + nums[l-1] >= target:
                    l -= 1
                
                # 检查是否等于目标值
                if nums[i] + nums[j] + nums[k] + nums[l] == target:
                    res.append([nums[i], nums[j], nums[k], nums[l]])
    
    return res

def main():
    import sys
    input = sys.stdin.read().split()
    idx = 0
    
    # 读取目标值和数组大小
    target = int(input[idx])
    idx += 1
    n = int(input[idx])
    idx += 1
    
    # 读取数组元素
    nums = list(map(int, input[idx:idx+n]))
    idx += n
    
    # 寻找四元组
    result = four_sum(nums, target)
    
    # 对结果排序
    result.sort()
    
    # 输出四元组
    for line in result:
        print('{0} {1} {2} {3}'.format(line[0], line[1], line[2], line[3]))

if __name__ == "__main__":
    main()