# NQ004 球体体积计算
import sys
def main():
    PI=3.1415926
    d=sys.stdin.read().split();i=0
    n=int(d[i]);i+=1  # 读取测试用例数量
    while n>0:
        r=float(d[i]);i+=1;n-=1
        v=(4.0/3.0)*PI*(r**3)  # 计算体积
        print('{0:.3f}'.format(v))  # 输出保留三位小数
if __name__=="__main__":main()