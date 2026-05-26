# NQ003: 平均数1
# 读取两个成绩A和B，权重分别为3.5和7.5，计算加权平均数，保留5位小数

a = float(input())
b = float(input())
avg = (a * 3.5 + b * 7.5) / 11.0
print(f"MEDIA = {avg:.5f}")
