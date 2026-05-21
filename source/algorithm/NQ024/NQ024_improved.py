# NQ024 珠穆朗玛峰测距
import math
def main():
    c=int(input())
    for _ in range(c):
        x,y,m,n=map(float,input().split())
        d=math.sqrt((x-m)**2+(y-n)**2)  # 计算欧几里得距离
        print("{0:.1f}".format(d))  # 输出保留一位小数
if __name__=="__main__":
    main()