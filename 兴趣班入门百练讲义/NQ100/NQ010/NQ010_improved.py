# NQ010 小鲁记账
import sys
def main():
    for line in sys.stdin:
        line=line.strip()
        if not line:continue
        parts=list(map(float,line.split()))
        n=int(parts[0])
        if n==0:break
        a,b,c=0,0,0  # a:负数, b:零, c:正数
        for num in parts[1:n+1]:
            if num==0:b+=1  # 统计零
            elif num<0:a+=1  # 统计负数
            else:c+=1  # 统计正数
        print("{} {} {}".format(a,b,c))  # 输出结果
if __name__=="__main__":main()