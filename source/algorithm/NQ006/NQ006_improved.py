# NQ006 成绩分区
import sys
def main():
    for line in sys.stdin:
        line=line.strip()
        if not line:continue
        s=float(line)
        if s<0 or s>100:print("Wrong Score!")
        elif s>=90:print("A:[90,100]")  # A级
        elif s>=80:print("B:[80,90)")   # B级
        elif s>=70:print("C:[70,80)")   # C级
        elif s>=60:print("D:[60,70)")   # D级
        else:print("E:[0,60)")         # E级
if __name__=="__main__":main()