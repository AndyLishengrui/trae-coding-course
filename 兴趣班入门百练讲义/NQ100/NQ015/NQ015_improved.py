# NQ015 辩论赛评分
import sys
def solve():
    d=sys.stdin.read().split()
    if not d:return
    i=0
    while i<len(d):
        n=int(d[i]);i+=1
        min_s,max_s,sum_s=101.0,-1.0,0.0  # 初始化最小值、最大值和总和
        for _ in range(n):
            s=float(d[i]);i+=1
            if s<min_s:min_s=s  # 更新最小值
            if s>max_s:max_s=s  # 更新最大值
            sum_s+=s  # 累加总分
        avg=(sum_s-min_s-max_s)/(n-2)
        print('{0:.2f}'.format(avg))  # 输出平均分
if __name__=="__main__":
    solve()