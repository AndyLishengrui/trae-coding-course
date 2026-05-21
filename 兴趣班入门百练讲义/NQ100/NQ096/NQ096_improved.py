N=9
MAX_ARRAY=1<<N # 512
BLANK='0'

row=[0]*N
col=[0]*N
cell=[[0 for _ in range(3)] for _ in range(3)]
ones=[0]*MAX_ARRAY
lowbit2pos=[0]*MAX_ARRAY
sudoku=[]

def lowbit(x):
    return x&-x

def clear_bit(x,n):
    return x&~(1<<n)

def set_bit(x,n):
    return x|(1<<n)

def get_available(x,y):
    return row[x]&col[y]&cell[x//3][y//3]

def init():
    for i in range(N):
        row[i]=col[i]=MAX_ARRAY-1
    for i in range(3):
        for j in range(3):
            cell[i][j]=MAX_ARRAY-1

def precompute():
    for i in range(N):
        lowbit2pos[1<<i]=i
    for i in range(MAX_ARRAY):
        cnt=0
        j=i
        while j:
            cnt+=1
            j-=lowbit(j)
        ones[i]=cnt

def read_sudoku():
    grid=[]
    for _ in range(N):
        line=input().strip()
        grid.append(list(line))
    return grid

def print_sudoku(grid):
    for row in grid:
        print(''.join(row))

def dfs(empty):
    if empty==0:
        return True
    min_opts=float('inf')
    x,y=-1,-1
    for i in range(N):
        for j in range(N):
            if sudoku[i][j]==BLANK:
                opts=ones[get_available(i,j)]
                if opts<min_opts:
                    min_opts=opts
                    x=i
                    y=j
    avail=get_available(x,y)
    sk=avail
    while sk:
        bit=lowbit(sk)
        num=lowbit2pos[bit] # 0-8，对应数字1-9
        row[x]=clear_bit(row[x],num)
        col[y]=clear_bit(col[y],num)
        cell[x//3][y//3]=clear_bit(cell[x//3][y//3],num)
        sudoku[x][y]=str(num+1)
        if dfs(empty-1):
            return True
        sudoku[x][y]=BLANK
        row[x]=set_bit(row[x],num)
        col[y]=set_bit(col[y],num)
        cell[x//3][y//3]=set_bit(cell[x//3][y//3],num)
        sk-=bit
    return False

def main():
    precompute()
    global sudoku
    sudoku=read_sudoku()
    init()
    empty=0
    for i in range(N):
        for j in range(N):
            if sudoku[i][j]==BLANK:
                empty+=1
            else:
                num=int(sudoku[i][j])-1
                row[i]=clear_bit(row[i],num)
                col[j]=clear_bit(col[j],num)
                cell[i//3][j//3]=clear_bit(cell[i//3][j//3],num)
    dfs(empty)
    print_sudoku(sudoku)

if __name__=="__main__":
    main()