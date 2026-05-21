import sys

def f(n):
    if n < 10:
        return chr(n + ord('0'))
    else:
        return chr(n - 10 + ord('A'))

def main():
    # 打表法
    P = ['' for _ in range(36)]
    for i in range(36):
        P[i] = f(i)
    
    # 完成p进制的转换
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        parts = line.split()
        if len(parts) != 2:
            continue
        n = int(parts[0])
        p = int(parts[1])
        
        if p > 36 or p <= 1:
            continue  # 越界忽略
        
        minus = 0
        if n < 0:
            minus = -1
            n = -n
        
        a = []
        while n:
            a.append(f(n % p))  # 转换位相应位数
            n //= p
        
        if minus < 0:
            print('-', end='')
        for c in reversed(a):
            print(c, end='')
        print()

if __name__ == "__main__":
    main()
