# NQ009 计算偶数平方和和奇数立方和
import sys
def main():
    for line in sys.stdin:
        line=line.strip()
        if not line:continue
        a,b=map(int,line.split())
        s1=0;s2=0  # s1:偶数平方和, s2:奇数立方和
        for i in range(a,b+1):
            if i%2==0:s1+=i*i  # 偶数平方累加
            else:s2+=i*i*i     # 奇数立方累加
        print(s1,s2)  # 输出结果
if __name__=="__main__":main()