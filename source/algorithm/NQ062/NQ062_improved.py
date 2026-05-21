import sys

def lowbit(x):
    """计算x的二进制中最后一个1所构成的整数"""
    return x & -x

def count_ones(x):
    """计算x的二进制中1的个数"""
    res = 0
    # 每次减去x的最后一个1，直到x为0
    while x:
        x -= lowbit(x)
        res += 1
    return res

def main():
    input = sys.stdin.read().split()
    n = int(input[0])
    nums = list(map(int, input[1:n+1]))
    
    # 计算每个数的二进制中1的个数
    results = [count_ones(num) for num in nums]
    
    # 输出结果，用空格连接
    print(' '.join(map(str, results)))

if __name__ == "__main__":
    main()