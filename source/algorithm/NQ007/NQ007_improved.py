# NQ007 一年中的第几天
import sys
d=[0,31,28,31,30,31,30,31,31,30,31,30,31]  # 每月天数
def is_leap(y):return (y%4==0 and y%100!=0) or (y%400==0)  # 判断闰年
def main():
    for line in sys.stdin:
        line=line.strip()
        if not line:continue
        y,m,day=map(int,line.split('/'))
        t=day
        for i in range(1,m):t+=d[i]
        if is_leap(y) and m>2:t+=1  # 闰年2月多一天
        print(t)
if __name__=="__main__":main()