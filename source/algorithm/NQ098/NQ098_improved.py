N = 9
MAXN = 1 << N  # 512

ones = [0] * MAXN
LOG2 = [0] * MAXN
row = [0] * N
col = [0] * N
cell = [[0 for _ in range(3)] for _ in range(3)]
sudoku = [[0 for _ in range(N)] for _ in range(N)]
max_score = -1

def lowbit(x):
    return x & -x

def init():
    # 初始化LOG2和ones数组
    for i in range(N):
        LOG2[1 << i] = i
    for i in range(MAXN):
        ones[i] = 0
        j = i
        while j:
            ones[i] += 1
            j -= lowbit(j)
    # 初始化状态数组
    for i in range(N):
        row[i] = col[i] = MAXN - 1
    for i in range(3):
        for j in range(3):
            cell[i][j] = MAXN - 1

def get_score(x, y, t):
    dist = min(min(x, 8 - x), min(y, 8 - y))
    return (dist + 6) * t

def get_avail(x, y):
    return row[x] & col[y] & cell[x // 3][y // 3]

def flip(x, y, n):
    row[x] ^= 1 << n
    col[y] ^= 1 << n
    cell[x // 3][y // 3] ^= 1 << n

def dfs(left, score):
    global max_score
    if left == 0:
        if score > max_score:
            max_score = score
        return
    
    # 找到可选数字最少的格子
    min_opts = float('inf')
    x, y = -1, -1
    for i in range(N):
        for j in range(N):
            if sudoku[i][j] == 0:
                opts = ones[get_avail(i, j)]
                if opts < min_opts:
                    min_opts = opts
                    x = i
                    y = j
    
    # 尝试填入每个可能的数字
    avail = get_avail(x, y)
    sk = avail
    while sk:
        bit = lowbit(sk)
        num = LOG2[bit]  # 0-8，对应数字1-9
        val = num + 1
        
        # 修改状态
        sudoku[x][y] = val
        flip(x, y, num)
        new_score = score + get_score(x, y, val)
        
        dfs(left - 1, new_score)
        
        # 回溯
        sudoku[x][y] = 0
        flip(x, y, num)
        
        sk -= bit

def main():
    global max_score
    init()
    
    left = 0
    initial_score = 0
    
    for i in range(N):
        line = list(map(int, input().split()))
        for j in range(N):
            t = line[j]
            sudoku[i][j] = t
            if t != 0:
                num = t - 1
                flip(i, j, num)
                initial_score += get_score(i, j, t)
            else:
                left += 1
    
    dfs(left, initial_score)
    print(max_score)

if __name__ == "__main__":
    main()