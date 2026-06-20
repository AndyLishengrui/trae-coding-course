# NQ1-06: 油耗
# 输入行驶距离和消耗汽油量，计算每升公里数，保留3位小数。

distance = float(input())  # 行驶距离 (km)
fuel = float(input())      # 消耗汽油量 (L)
print(f"{distance / fuel:.3f} km/l")
