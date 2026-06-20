# 钱庄换银：贪心换零钱
n = int(input())
print(n)
denoms = [100, 50, 20, 10, 5, 2, 1]
for d in denoms:
    print(f"{n // d} nota(s) de R$ {d},00")
    n %= d
