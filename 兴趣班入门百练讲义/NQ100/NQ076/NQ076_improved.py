def qmi(a, k, p):
    res = 1  # 初始值为1
    while k:
        if k & 1:  # b的最末尾为1
            res = res * a % p
        k >>= 1  # 去掉b最低位
        a = a * a % p
    return res

def main():
    import sys
    q = int(sys.stdin.readline())
    for _ in range(q):
        a, k, p = map(int, sys.stdin.readline().split())
        print(qmi(a, k, p))

if __name__ == "__main__":
    main()
