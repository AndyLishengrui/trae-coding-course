# NQ012 水仙花数
import sys
def main():
    # 逐行读取输入
    for line in sys.stdin:
        # 去除行首尾空白
        line=line.strip()
        # 跳过空行
        if not line:continue
        # 解析输入的m和n
        m,n=map(int,line.split())
        # 存储水仙花数的列表
        res=[]
        # 遍历从m到n的所有数
        for i in range(m,n+1):
            # 分解数字的百位、十位和个位
            a=i//100;b=i%100//10;c=i%10
            # 计算各位数字的立方和
            sum_c=a*a*a + b*b*b + c*c*c
            # 判断是否为水仙花数，如果是则添加到结果列表
            if sum_c==i:res.append(str(i))
        # 如果有水仙花数，用空格连接输出
        if res:print(' '.join(res))
        # 否则输出"no"
        else:print('no')
if __name__=="__main__":main()