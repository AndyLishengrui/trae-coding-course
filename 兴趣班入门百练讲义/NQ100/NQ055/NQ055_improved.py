import sys

def gcd(a, b):
    """求最大公约数（GCD）"""
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    """求最小公倍数（LCM）"""
    return (a * b) // gcd(a, b)

def main():
    input = sys.stdin.read().split()
    ptr = 0
    
    while ptr < len(input):
        n = int(input[ptr])
        ptr += 1
        if n <= 0:
            break
        
        result = 1
        for _ in range(n):
            num = int(input[ptr])
            ptr += 1
            result = lcm(result, num)  # 累积计算LCM
        
        print(result)

if __name__ == "__main__":
    main()