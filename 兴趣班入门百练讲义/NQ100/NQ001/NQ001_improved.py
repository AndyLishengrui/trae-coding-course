# NQ001 求连续整数和
import sys
def main():
    d=sys.stdin.read().split();p=0  # 读取所有输入并分割
    a=int(d[p]);p+=1  # 读取起始整数a
    n=0
    while True:  # 过滤非正整数n
        if p>=len(d):return
        n=int(d[p]);p+=1
        if n>0:break
    if n<=0:return
    r=0
    for _ in range(n):r+=a;a+=1  # 累加n个连续整数
    print(r)  # 输出结果
if __name__=="__main__":main()