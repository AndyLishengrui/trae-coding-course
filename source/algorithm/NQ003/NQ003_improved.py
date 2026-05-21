# NQ003 计算线段长度
import math,sys
def main():
    d=sys.stdin.read().split();i=0
    n=int(d[i]);i+=1  # 读取测试用例数量
    while n>0:
        x1,y1,x2,y2=map(float,d[i:i+4])
        i+=4;n-=1
        dx=x1-x2;dy=y1-y2
        dist=math.sqrt(dx*dx+dy*dy)  # 计算欧几里得距离
        print("%.2f"%dist)  # 输出保留两位小数
if __name__=="__main__":main()