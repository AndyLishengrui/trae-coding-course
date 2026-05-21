# NQ021 废强重建
import sys
first=True
while True:
    line=sys.stdin.readline()
    if not line:break
    n=int(line.strip())
    if n==0:break
    h=[]
    while len(h)<n:
        hl=sys.stdin.readline()
        if not hl:break
        h.extend(map(int,hl.strip().split()))
    total=sum(h)
    avg=total//n  # 计算平均值（向下取整）
    need=sum(avg-ht for ht in h if ht<avg)  # 统计需要的砖块数
    if not first:print()
    print(need)
    first=False