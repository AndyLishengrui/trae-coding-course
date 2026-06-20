# NQ1-11: 简单计算
# 输入产品编号、数量和单价，计算应付总额。

code, quantity = map(int, input().split())
price = float(input())
print(f"VALOR A PAGAR: R$ {quantity * price:.2f}")
