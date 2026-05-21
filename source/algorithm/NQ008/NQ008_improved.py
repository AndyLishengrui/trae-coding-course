import sys
def main():
    for line in sys.stdin:
        line=line.strip()
        if not line:continue
        parts=list(map(int,line.split()))
        if len(parts)<2:print(1);continue
        m=parts[0];nums=parts[1:m+1]
        res=1
        for x in nums:
            if x%2:res*=x  # 累乘奇数
        print(res)  # 输出结果
if __name__=="__main__":main()