import sys
N = 9
M = 1 << N
ones = [0] * M
map_bit = [0] * M
row = [0] * N
col = [0] * N
cell = [[0] * 3 for _ in range(3)]
g = [[0] * N for _ in range(N)]
ans = -1
def lowbit(x):
    """获取最低位的1"""
    return x & -x
def init():
    """初始化位运算相关数组"""
    for i in range(N):
        map_bit[1 << i] = i
    for i in range(M):
        cnt = 0
        j = i
        while j:
            cnt += 1
            j -= lowbit(j)
        ones[i] = cnt
    # 初始化行、列和单元格的状态，所有位都为1（表示可以填任何数字）
    for i in range(9):
        row[i] = col[i] = cell[i//3][i%3] = M - 1
def get_score(x, y, t):
    """计算填入数字t到(x,y)位置的得分"""
    return (min(min(x, 8 - x), min(y, 8 - y)) + 6) * t
def draw(x, y, t):
    """在(x,y)位置填入或删除数字t"""
    s = 1
    if t > 0:
        g[x][y] = t
    else:
        s = -1
        t = -t
        g[x][y] = 0
    t -= 1  # 转换为0-8的索引
    row[x] -= (1 << t) * s
    col[y] -= (1 << t) * s
    cell[x//3][y//3] -= (1 << t) * s
def get(x, y):
    """获取(x,y)位置可以填入的数字的位掩码"""
    return row[x] & col[y] & cell[x//3][y//3]
def dfs(cnt, score):
    """深度优先搜索填充数独"""
    global ans
    if cnt == 0:
        if score > ans:
            ans = score
        return
    # 找到可填数字最少的位置，优化搜索顺序
    minv = 10
    x, y = -1, -1
    for i in range(N):
        for j in range(N):
            if g[i][j] == 0:
                t = ones[get(i, j)]
                if t < minv:
                    minv = t
                    x, y = i, j
    # 尝试填入所有可能的数字
    mask = get(x, y)
    while mask:
        lb = lowbit(mask)
        t = map_bit[lb] + 1  # 转换为1-9的数字
        draw(x, y, t)
        dfs(cnt - 1, score + get_score(x, y, t))
        draw(x, y, -t)  # 回溯
        mask -= lb
def main():
    global ans
    init()
    cnt = 0
    score = 0
    # 读取输入
    for i in range(N):
        line = sys.stdin.readline().strip()
        if not line:
            continue
        nums = list(map(int, line.split()))
        for j in range(N):
            x = nums[j]
            if x:
                draw(i, j, x)
                score += get_score(i, j, x)
            else:
                cnt += 1
    # 开始深度优先搜索
    dfs(cnt, score)
    # 输出最高得分
    print(ans)
if __name__ == "__main__":
    main()