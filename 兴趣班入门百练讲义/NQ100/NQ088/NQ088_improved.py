# Python equivalent of the optimized C++ code
# 最长不上升子序列问题（优化版）
import sys
def main():
    # Read input
    n = int(sys.stdin.readline())
    heights = list(map(int, sys.stdin.readline().split()))
    # 优化算法：贪心 + 二分查找 O(n log n)
    tails = []
    for h in heights:
        # 找到第一个小于h的位置（因为是不上升，所以找第一个小于h的位置）
        left, right = 0, len(tails)
        while left < right:
            mid = (left + right) // 2
            if tails[mid] < h:
                right = mid
            else:
                left = mid + 1
        if left == len(tails):
            tails.append(h)
        else:
            tails[left] = h
    print(len(tails))
if __name__ == "__main__":
    main()