import math

def main():
    t = int(input())
    for _ in range(t):
        s, u = map(float, input().split())
        v = 1.0 / math.tan(math.atan(1.0/s) - math.atan(1.0/u))  # 计算v值
        res = v*u - s*u - v*s  # 计算最终结果
        print("{0:.0f}".format(res))

if __name__ == "__main__":
    main()