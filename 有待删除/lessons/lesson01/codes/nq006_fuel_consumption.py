# NQ006: 油耗
# 输入行驶距离(km)和消耗的燃料(L)，计算每升燃料行驶的公里数

distance = float(input())  # 总距离（km）
fuel = float(input())      # 消耗的燃料（L）
efficiency = distance / fuel
print(f"{efficiency:.3f} km/l")
