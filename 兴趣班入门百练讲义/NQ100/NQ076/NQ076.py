# NQ076 二进制取幂法 Python 3.5 版本

def qmi(a, k, p):
    res = 1  # 初始值为1
    while k:
        if k & 1:  # k的最末尾为1
            res = res * a % p  # 计算并取模
        k >>= 1  # 去掉k最低位
        a = a * a % p  # 提前计算a的平方并取模
    return res

if __name__ == "__main__":
    q = int(input().strip())  # 读入q，表示有q组数据
    for _ in range(q):
        a, k, p = map(int, input().strip().split())  # 读入a, k, p
        print(qmi(a, k, p))  # 计算快速幂并输出结果