s=[]
def dfs(r,p):
    global s
    if r>7:
        s.append(p.copy())
        return
    for c in range(1,9):
        ok=1
        for i in range(r):
            if p[i]==c or abs(p[i]-c)==abs(r-i): ok=0; break  # 检查列和对角线冲突
        if ok:
            p[r]=c
            dfs(r+1,p)  # 放置皇后并递归

def pre():
    global s
    s=[]
    dfs(0,[0]*8)

def main():
    pre()  # 预处理所有8皇后解
    import sys
    inp=sys.stdin.read().splitlines()
    T=int(inp[0])
    for i in range(1,T+1):
        n=int(inp[i])
        if n<1 or n>92:
            print("Invalid input!")
            continue
        print(''.join(map(str,s[n-1])))  # 输出第n-1个解

if __name__=="__main__":
    main()
