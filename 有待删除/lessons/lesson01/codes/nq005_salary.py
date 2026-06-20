# NQ005: 工资
# 读取员工编号、工作时数、时薪，计算工资

number = int(input())
hours = int(input())
rate = float(input())
salary = hours * rate
print(f"NUMBER = {number}")
print(f"SALARY = U$ {salary:.2f}")
