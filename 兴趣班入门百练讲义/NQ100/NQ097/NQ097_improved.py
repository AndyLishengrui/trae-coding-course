N=9
MAXN=1<<N # 512
BLANK='.'

row=[0]*N
col=[0]*N
cell=[[0 for _ in range(3)] for _ in range(3)]
ones=[0]*MAXN
LOG2=[0]*MAXN
sudoku=[]

def lowbit(x):
    return x&-x

def count_ones(n):
    res=0
    while n:
        n-=lowbit(n)
        res+=1
    return res

def build_tables():
    for i in range(N):
        LOG2[1<<i]=i
    for i in range(MAXN):
        ones[i]=count_ones(i)

def init():
    for i in range(N):
        row[i]=col[i]=MAXN-1
    for i in range(3):
        for j in range(3):
            cell[i][j]=MAXN-1

def flip(x,y,n):
    row[x]^=1<<n
    col[y]^=1<<n
    cell[x//3][y//3]^=1<<n

def get_avail(x,y):
    return row[x]&col[y]&cell[x//3][y//3]

def dfs(empty):
    if empty==0:
        print(''.join(sudoku))
        return True
    min_opts=float('inf')
    x,y=-1,-1
    for i in range(N):
        for j in range(N):
            if sudoku[i*N+j]==BLANK:
                opts=ones[get_avail(i,j)]
                if opts<min_opts:
                    min_opts=opts
                    x=i
                    y=j
    avail=get_avail(x,y)
    sk=avail
    while sk:
        bit=lowbit(sk)
        num=LOG2[bit] # 0-8，对应数字1-9
        flip(x,y,num)
        sudoku[x*N+y]=str(num+1)
        dfs(empty-1)
        sudoku[x*N+y]=BLANK
        flip(x,y,num)
        sk-=bit
    return False

def main():
    build_tables()
    import sys
    for line in sys.stdin:
        line=line.strip()
        if not line:
            continue
        if line[0]=='e':
            break
        global sudoku
        sudoku=list(line)
        init()
        empty=0
        for i in range(N):
            for j in range(N):
                if sudoku[i*N+j]==BLANK:
                    empty+=1
                else:
                    num=int(sudoku[i*N+j])-1
                    flip(i,j,num)
        dfs(empty)

if __name__=="__main__":
    main()