# NQ016 十六进制加法
import sys
for line in sys.stdin:
    line=line.strip()
    if not line:continue
    parts=line.split()
    if len(parts)!=2:continue
    a=int(parts[0],16);b=int(parts[1],16)  # 十六进制转整数
    res=a+b
    if res<0:
        print('-'+hex(-res)[2:].upper())  # 负数处理
    else:
        print(hex(res)[2:].upper())  # 大写十六进制输出