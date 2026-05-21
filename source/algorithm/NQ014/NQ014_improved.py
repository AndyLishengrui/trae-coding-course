# NQ014 凤凰花开吃杨梅
def calc(n):
    res=1  # 第n天剩下1个
    for i in range(n-1,0,-1):
        res=(res+1)*2  # 逆推前一天的数量
    return res

def main():
    import sys
    for line in sys.stdin:
        line=line.strip()
        if not line:continue
        x=int(line)
        print(calc(x))  # 计算并输出

if __name__=="__main__":main()