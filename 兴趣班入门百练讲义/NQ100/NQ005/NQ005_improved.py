# NQ005 实数绝对值
import sys
def main():
    for line in sys.stdin:
        line=line.strip()
        if not line:continue
        x=float(line)
        v=abs(x)  # 计算绝对值
        print("%.2f"%v)  # 输出保留两位小数
if __name__=="__main__":main()