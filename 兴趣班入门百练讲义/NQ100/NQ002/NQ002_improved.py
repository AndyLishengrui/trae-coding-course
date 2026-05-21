# NQ002 字符比大小
import sys
def main():
    d=sys.stdin.read().split()
    n=int(d[0])  # 读取数据组数
    for i in range(1,n+1):
        line=d[i]
        chars=sorted(line[:3])  # 取前3个字符并排序
        print('{} {} {}'.format(chars[0], chars[1], chars[2]))
if __name__=="__main__":main()