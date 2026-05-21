#!/usr/bin/env python3
# NQ060 四元组求和
import sys

def four_sum(nums, target):
    res = []
    # 排序数组
    nums.sort()
    n = len(nums)
    
    # 四重循环，后两重用双指针
    for i in range(n):
        # 跳过重复的i值
        if i > 0 and nums[i] == nums[i-1]:
            continue
        
        for j in range(i + 1, n):
            # 跳过重复的j值
            if j > i + 1 and nums[j] == nums[j-1]:
                continue
            
            # 双指针算法
            k = j + 1
            l = n - 1
            
            while k < l:
                # 跳过重复的k值
                if k > j + 1 and nums[k] == nums[k-1]:
                    k += 1
                    continue
                
                # 移动l指针到合适的位置
                while k < l - 1 and nums[i] + nums[j] + nums[k] + nums[l-1] >= target:
                    l -= 1
                
                # 检查是否找到和为目标值的四元组
                current_sum = nums[i] + nums[j] + nums[k] + nums[l]
                if current_sum == target:
                    res.append([nums[i], nums[j], nums[k], nums[l]])
                    k += 1
                elif current_sum < target:
                    k += 1
                else:
                    l -= 1
    
    return res

def main():
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        # 读取目标值和数组长度
        target, n = map(int, line.split())
        # 读取数组元素
        nums_line = sys.stdin.readline().strip()
        if not nums_line:
            break
        nums = list(map(int, nums_line.split()))
        # 寻找四元组
        res = four_sum(nums, target)
        # 对结果排序
        res.sort()
        # 输出结果
        for quadruplet in res:
            print(' '.join(map(str, quadruplet)))

if __name__ == "__main__":
    main()