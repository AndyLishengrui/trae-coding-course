# NQ023 桌球比赛
import sys
def main():
    s=[]
    for l in sys.stdin:
        l=l.strip()
        if l:s.append(l) if l.isdigit() else s.extend(list(l))
    p=0
    while p<len(s):
        if not s[p].isdigit():
            p+=1
            continue
        m=int(s[p]);p+=1
        if m<=0:continue
        r,y=0,0
        for _ in range(m):
            if p>=len(s):break
            c=s[p];p+=1
            if c=='R':r+=1
            elif c=='Y':y+=1
            elif c=='B':print("Red" if r==7 else "Yellow")
            elif c=='L':print("Yellow" if y==7 else "Red")
if __name__=="__main__":main()