# NQ009: 时间转换
n = int(input())
h = n // 3600
m = n % 3600 // 60
s = n % 60
print(f"{h}:{m}:{s}")
