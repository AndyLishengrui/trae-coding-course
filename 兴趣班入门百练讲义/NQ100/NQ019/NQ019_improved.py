# NQ019 最大公约数
def gcd(a,b):
    while b:a,b=b,a%b
    return a
n=int(input())
for _ in range(n):
    a,b=map(int,input().split())
    print(gcd(a,b))