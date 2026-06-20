# NQ1-08: 钞票
# 贪心算法: 用最少的钞票数量支付金额N。

n = int(input())
bills = [100, 50, 20, 10, 5, 2, 1]  # 面额从大到小

print(n)
for value in bills:
    print(f"{n // value} nota(s) de R$ {value},00")
    n %= value
