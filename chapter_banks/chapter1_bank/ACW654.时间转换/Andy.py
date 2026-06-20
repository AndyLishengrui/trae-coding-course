# NQ1-09: 时间转换
# 将总秒数N转换为 HH:MM:SS 格式。

n = int(input())

hours, remainder = divmod(n, 3600)
minutes, seconds = divmod(remainder, 60)

print(f"{hours}:{minutes}:{seconds}")
