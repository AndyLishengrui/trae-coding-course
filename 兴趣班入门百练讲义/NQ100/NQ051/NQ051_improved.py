import sys

def main():
    input = sys.stdin.read().split()
    ptr = 0
    
    while ptr < len(input):
        n = int(input[ptr])
        ptr += 1
        if n <= 0:
            break
        
        nums = list(map(int, input[ptr:ptr+n]))
        ptr += n
        
        # 找到最小值及其下标
        min_idx = nums.index(min(nums))
        
        # 交换最小值与第一个元素
        if min_idx != 0:
            nums[0], nums[min_idx] = nums[min_idx], nums[0]
        
        # 输出交换后的数组
        print(' '.join(map(str, nums)))

if __name__ == "__main__":
    main()