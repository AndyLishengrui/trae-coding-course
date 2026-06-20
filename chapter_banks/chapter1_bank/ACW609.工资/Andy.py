# NQ1-05: 工资
# 输入员工编号、工作时数和时薪，计算工资总额。

number = int(input())   # 员工编号
hours = int(input())    # 月工作时数
rate = float(input())   # 时薪
print(f"NUMBER = {number}")
print(f"SALARY = U$ {hours * rate:.2f}")
