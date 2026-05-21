# NQ017 计算绩点
q=int(input())
tc=0.0;tg=0.0
for _ in range(q):
    s,c=map(float,input().split())
    # 根据成绩计算绩点
    if s>=90:g=4.0
    elif s>=85:g=3.7
    elif s>=81:g=3.3
    elif s>=78:g=3.0
    elif s>=75:g=2.7
    elif s>=72:g=2.3
    elif s>=68:g=2.0
    elif s>=64:g=1.7
    elif s>=60:g=1.0
    else:g=0.0
    tc+=c;tg+=g*c  # 累加学分和加权绩点
print('{0:.4f}'.format(tg/tc))  # 输出加权平均绩点