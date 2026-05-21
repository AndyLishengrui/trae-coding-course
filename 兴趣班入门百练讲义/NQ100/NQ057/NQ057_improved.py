import sys
import math

def main():
    for line in sys.stdin:
        n = int(line.strip())
        # 灯泡亮着的数量等于n以内的完全平方数个数
        # 即n的平方根的整数部分
        print(int(math.isqrt(n)))

if __name__ == "__main__":
    main()