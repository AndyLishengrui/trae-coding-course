# 集市算账：编号×数量，第二行单价
id_num, qty = map(int, input().split())
price = float(input())
print(f"TOTAL = {qty * price:.2f}")
