# NQ022 竞选投票
n=int(input())
h=list(map(int,input().split()))
r=[x//2+1 for x in h]  # 每个班级需要超过半数的票数
r.sort()
need=n//2+1  # 需要超过半数的班级支持
total=sum(r[:need])  # 取所需班级数的最小票数
print(total)