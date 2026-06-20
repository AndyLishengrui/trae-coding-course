# NQ1-04: 平均数1
# 加权平均分: A(权重3.5) + B(权重7.5)，保留5位小数。

a = float(input())  # 学生A的成绩
b = float(input())  # 学生B的成绩
print(f"MEDIA = {(a * 3.5 + b * 7.5) / 11.0:.5f}")
