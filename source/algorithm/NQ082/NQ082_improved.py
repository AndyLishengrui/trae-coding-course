def divide(n):
    i = 2
    while i * i <= n:
        if n % i == 0:
            count = 0
            while n % i == 0:
                n //= i
                count += 1
            print(i, count)  # 输出质因数及其指数
        i += 1
    if n > 1:
        print(n, 1)  # 处理剩余的质因数
    print()  # 分隔不同测试用例

def main():
    import sys
    n = int(sys.stdin.readline())
    for _ in range(n):
        a = int(sys.stdin.readline())
        divide(a)  # 分解质因数

if __name__ == "__main__":
    main()
