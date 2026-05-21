import sys

EPS = 1e-6
N = 4

def is_zero(x):
    return abs(x) <= EPS

def count24(nums):
    n = len(nums)
    if n == 1:
        return is_zero(nums[0] - 24)
    
    for i in range(n - 1):
        for j in range(i + 1, n):
            next_nums = []
            for k in range(n):
                if k != i and k != j:
                    next_nums.append(nums[k])
            
            # 加法
            next_nums.append(nums[i] + nums[j])
            if count24(next_nums):
                return True
            next_nums.pop()
            
            # 乘法
            next_nums.append(nums[i] * nums[j])
            if count24(next_nums):
                return True
            next_nums.pop()
            
            # 减法
            next_nums.append(nums[i] - nums[j])
            if count24(next_nums):
                return True
            next_nums.pop()
            
            # 减法 (交换顺序)
            next_nums.append(nums[j] - nums[i])
            if count24(next_nums):
                return True
            next_nums.pop()
            
            # 除法
            if not is_zero(nums[j]):
                next_nums.append(nums[i] / nums[j])
                if count24(next_nums):
                    return True
                next_nums.pop()
            
            # 除法 (交换顺序)
            if not is_zero(nums[i]):
                next_nums.append(nums[j] / nums[i])
                if count24(next_nums):
                    return True
                next_nums.pop()
    
    return False

def main():
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        nums = list(map(float, line.split()))
        if len(nums) != N:
            continue
        
        # 检查是否全为0
        is_end = True
        for num in nums:
            if not is_zero(num):
                is_end = False
                break
        if is_end:
            break
        
        if count24(nums):
            print("YES")
        else:
            print("NO")

if __name__ == "__main__":
    main()
