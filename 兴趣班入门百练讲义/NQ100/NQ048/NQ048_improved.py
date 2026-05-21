import sys

def main():
    candidate = None
    count = 0
    
    # 读取所有输入数据
    data = list(map(int, sys.stdin.read().split()))
    
    # 摩尔投票算法寻找多数元素
    for x in data:
        if count == 0:
            candidate = x  # 当计数器为0时，设置新的候选元素
            count = 1
        elif candidate == x:
            count += 1  # 当前元素与候选元素相同，计数器加1
        else:
            count -= 1  # 当前元素与候选元素不同，计数器减1
    
    # 输出多数元素
    print(candidate)

if __name__ == "__main__":
    main()