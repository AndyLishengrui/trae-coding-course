# NQ100 滚石柱 - 改进版
# Python 3.5 兼容
from collections import deque

MAX_N = 507

class Stone:
    def __init__(self, x=0, y=0, status=0):
        self.x = x
        self.y = y
        self.status = status  # 0为站立 1为横躺 2为竖躺

# 四种方向 UP=0, DOWN=1, LEFT=2, RIGHT=3
# 每种状态的坐标以方块的左上顶点的格子为基准点
direction = [
    # UP
    [[-2, 0, 2], [-1, 0, 1], [-1, 0, 0]],
    # DOWN
    [[1, 0, 2], [1, 0, 1], [2, 0, 0]],
    # LEFT
    [[0, -2, 1], [0, -1, 0], [0, -1, 2]],
    # RIGHT
    [[0, 1, 1], [0, 2, 0], [0, 1, 2]]
]

def is_inside(x, y, n, m):
    return 0 <= x < n and 0 <= y < m

def is_valid(node, target, area, n, m):
    # 检查基准点是否合法
    if not is_inside(node.x, node.y, n, m) or area[node.x][node.y] == '#':
        return False
    
    # 检查不同状态下的其他格子
    if node.status == 1:  # 横躺，需要检查右侧格子
        if not is_inside(node.x, node.y + 1, n, m) or area[node.x][node.y + 1] == '#':
            return False
    elif node.status == 2:  # 竖躺，需要检查下方格子
        if not is_inside(node.x + 1, node.y, n, m) or area[node.x + 1][node.y] == '#':
            return False
    
    # 终点必须是站立状态
    if node.x == target.x and node.y == target.y and node.status != 0:
        return False
    
    return True

def move_stone(p, dir):
    dx = direction[dir][p.status][0]
    dy = direction[dir][p.status][1]
    new_status = direction[dir][p.status][2]
    return Stone(p.x + dx, p.y + dy, new_status)

def build_map(n, m):
    area = []
    start = Stone()
    target = Stone()
    
    for i in range(n):
        line = input().strip()
        area.append(list(line))
    
    # 寻找起点和终点
    for i in range(n):
        for j in range(m):
            if area[i][j] == 'X':
                start = Stone(i, j, 0)
                area[i][j] = '.'
                
                # 检查是否是横躺或竖躺
                if is_inside(i, j + 1, n, m) and area[i][j + 1] == 'X':
                    start.status = 1
                    area[i][j + 1] = '.'
                elif is_inside(i + 1, j, n, m) and area[i + 1][j] == 'X':
                    start.status = 2
                    area[i + 1][j] = '.'
            elif area[i][j] == 'O':
                target = Stone(i, j, 0)
    
    return area, start, target

def bfs(n, m, area, start, target):
    # 初始化距离数组
    dist = [[[-1 for _ in range(3)] for __ in range(m)] for ___ in range(n)]
    q = deque()
    
    q.append(start)
    dist[start.x][start.y][start.status] = 0
    
    while q:
        current = q.popleft()
        
        # 检查是否到达终点
        if current.x == target.x and current.y == target.y and current.status == 0:
            return dist[current.x][current.y][current.status]
        
        # 尝试四个方向
        for dir in range(4):
            next_stone = move_stone(current, dir)
            
            if is_valid(next_stone, target, area, n, m) and dist[next_stone.x][next_stone.y][next_stone.status] == -1:
                dist[next_stone.x][next_stone.y][next_stone.status] = dist[current.x][current.y][current.status] + 1
                q.append(next_stone)
    
    return -1  # 无法到达

def main():
    import sys
    input = sys.stdin.read().split('\n')
    idx = 0
    
    while True:
        if idx >= len(input):
            break
        line = input[idx].strip()
        while not line:
            idx += 1
            if idx >= len(input):
                break
            line = input[idx].strip()
        if idx >= len(input):
            break
        
        parts = line.split()
        if len(parts) < 2:
            idx += 1
            continue
        n = int(parts[0])
        m = int(parts[1])
        
        if n == 0:
            break
        
        idx += 1
        # 读取地图
        map_lines = []
        for _ in range(n):
            while idx < len(input) and not input[idx].strip():
                idx += 1
            if idx < len(input):
                map_lines.append(input[idx].strip())
                idx += 1
        
        # 重建输入流
        import io
        old_stdin = sys.stdin
        sys.stdin = io.StringIO('\n'.join(map_lines))
        
        area, start, target = build_map(n, m)
        result = bfs(n, m, area, start, target)
        
        sys.stdin = old_stdin
        
        if result == -1:
            print("Impossible")
        else:
            print(result)

if __name__ == "__main__":
    main()