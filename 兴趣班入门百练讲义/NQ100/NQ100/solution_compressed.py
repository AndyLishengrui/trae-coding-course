#!/usr/bin/env python3
# NQ100 滚石柱
import sys
from collections import deque

# 定义方向：UP=0, DOWN=1, LEFT=2, RIGHT=3
# 每个方向对应三种状态的变化：dx, dy, new_status
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

class Stone:
    """石柱类"""
    def __init__(self, x=0, y=0, status=0):
        self.x = x
        self.y = y
        self.status = status
    
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y and self.status == other.status
    
    def __hash__(self):
        return hash((self.x, self.y, self.status))

def move_stone(p, udlf):
    """根据方向移动石柱，返回新的石柱状态"""
    dx = direction[udlf][p.status][0]
    dy = direction[udlf][p.status][1]
    new_status = direction[udlf][p.status][2]
    return Stone(p.x + dx, p.y + dy, new_status)

def is_inside(x, y, n, m):
    return 0 <= x < n and 0 <= y < m

def is_valid(node, n, m, area):
    """判断石柱状态是否有效"""
    if not is_inside(node.x, node.y, n, m) or area[node.x][node.y] == '#':
        return False
    # 检查竖躺状态
    if node.status == 2:
        if not is_inside(node.x + 1, node.y, n, m) or area[node.x + 1][node.y] == '#':
            return False
    # 检查横躺状态
    if node.status == 1:
        if not is_inside(node.x, node.y + 1, n, m) or area[node.x][node.y + 1] == '#':
            return False
    if node.status == 0 and area[node.x][node.y] == 'E':
        return False
    return True

def build_map(n, m):
    """构建地图并找到起点和终点"""
    area = []
    start = Stone()
    target = Stone()
    
    for i in range(n):
        line = sys.stdin.readline().strip()
        filtered_line = []
        for c in line:
            if c in ['#', '.', 'X', 'O', 'E']:
                filtered_line.append(c)
        area.append(filtered_line)
    
    # 寻找起点和终点
    for i in range(n):
        for j in range(m):
            c = area[i][j]
            if c == 'X':
                start.x = i
                start.y = j
                start.status = 0
                area[i][j] = '.'
                if is_inside(i, j+1, n, m) and area[i][j+1] == 'X':
                    start.status = 1
                    area[i][j+1] = '.'
                elif is_inside(i+1, j, n, m) and area[i+1][j] == 'X':
                    start.status = 2
                    area[i+1][j] = '.'
            elif c == 'O':
                target.x = i
                target.y = j
                target.status = 0
    
    return area, start, target

def bfs(start, target, n, m, area):
    """广度优先搜索最短路径"""
    dist = [[[-1 for _ in range(3)] for __ in range(m)] for ___ in range(n)]
    q = deque()
    q.append(start)
    dist[start.x][start.y][start.status] = 0
    
    while q:
        current = q.popleft()
        
        # 尝试四个方向
        for i in range(4):
            next_stone = move_stone(current, i)
            
            if is_valid(next_stone, n, m, area) and dist[next_stone.x][next_stone.y][next_stone.status] == -1:
                dist[next_stone.x][next_stone.y][next_stone.status] = dist[current.x][current.y][current.status] + 1
                
                # 检查是否到达终点
                if next_stone.x == target.x and next_stone.y == target.y and next_stone.status == target.status:
                    return dist[next_stone.x][next_stone.y][next_stone.status]
                
                q.append(next_stone)
    
    return -1

def main():
    while True:
        line = sys.stdin.readline().strip()
        if not line:
            continue
        n, m = map(int, line.split())
        if n == 0:
            break
        
        area, start, target = build_map(n, m)
        res = bfs(start, target, n, m, area)
        
        if res == -1:
            print("Impossible")
        else:
            print(res)

if __name__ == "__main__":
    main()
