import sys

def main():
    input = sys.stdin.read().split()
    ptr = 0
    T = int(input[ptr])
    ptr += 1
    
    for _ in range(T):
        n = int(input[ptr])
        ptr += 1
        nums = list(map(int, input[ptr:ptr+n]))  # 严格读取n个数字
        ptr += n
        nums.sort()  # 对数组进行排序
        print(' '.join(map(str, nums)))  # 输出排序结果，用空格连接

if __name__ == "__main__":
    main()
