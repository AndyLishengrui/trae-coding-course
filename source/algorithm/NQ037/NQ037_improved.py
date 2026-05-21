# NQ037 按绝对值排序
def main():
    import sys
    input_data = list(map(int, sys.stdin.read().split()))
    ptr = 0
    n = input_data[ptr]
    ptr += 1
    for _ in range(n):
        m = input_data[ptr]
        ptr += 1
        nums = input_data[ptr:ptr + m]
        ptr += m
        sorted_nums = sorted(nums, key=abs, reverse=True)  # 按绝对值从大到小排序
        print(' '.join(map(str, sorted_nums)))

if __name__ == "__main__":
    main()