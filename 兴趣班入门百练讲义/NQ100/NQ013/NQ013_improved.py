# NQ013 倒数数列求和
MAX_N=10007
a=[0.0]*MAX_N
a[1]=1.0  # 第一项为1
for i in range(2,MAX_N):
    if i%2!=0:a[i]=a[i-1]+1.0/i  # 奇数项：加
    else:a[i]=a[i-1]-1.0/i       # 偶数项：减

def main():
    import sys
    inp=sys.stdin.read().split();i=0
    while i<len(inp):
        q=int(inp[i]);i+=1
        for _ in range(q):
            n=int(inp[i]);i+=1
            print('%.2f'%a[n])  # 输出保留两位小数
if __name__=="__main__":main()