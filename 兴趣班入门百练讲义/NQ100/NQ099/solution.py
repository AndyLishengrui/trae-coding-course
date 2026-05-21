#!/usr/bin/env python3
# NQ099 最省赛程
import sys
import heapq

class Node:
    """优先队列中的节点"""
    def __init__(self, city, fuel, money):
        self.city = city
        self.fuel = fuel
        self.money = money
    
    def __lt__(self, other):
        """定义小于运算符，使优先队列成为最小堆"""
        return self.money < other.money

def main():
    # 读取输入
    input_lines = [line.strip() for line in sys.stdin if line.strip()]
    ptr = 0
    
    # 读取城市数和道路数
    n, m = map(int, input_lines[ptr].split())
    ptr += 1
    
    # 读取每个城市的油价
    oil_price = list(map(int, input_lines[ptr].split()))
    ptr += 1
    
    # 构建邻接表
    adj = [[] for _ in range(n)]
    for _ in range(m):
        u, v, d = map(int, input_lines[ptr].split())
        ptr += 1
        adj[u].append((v, d))
        adj[v].append((u, d))
    
    # 读取查询数量
    q = int(input_lines[ptr])
    ptr += 1
    
    # 处理每个查询
    for _ in range(q):
        c, s, e = map(int, input_lines[ptr].split())
        ptr += 1
        
        # 初始化费用数组，expenses[city][fuel]表示到达city时剩余fuel的最小花费
        INF = float('inf')
        expenses = [[INF] * (c + 1) for _ in range(n)]
        visited = [[False] * (c + 1) for _ in range(n)]
        
        # 优先队列
        heap = []
        # 起点状态：城市s，油量0，花费0
        expenses[s][0] = 0
        heapq.heappush(heap, Node(s, 0, 0))
        
        found = False
        while heap:
            current = heapq.heappop(heap)
            city = current.city
            fuel = current.fuel
            money = current.money
            
            # 如果已经访问过这个状态，跳过
            if visited[city][fuel]:
                continue
            visited[city][fuel] = True
            
            # 如果到达终点
            if city == e:
                print(money)
                found = True
                break
            
            # 选项1：在当前城市加1升油
            if fuel < c:
                new_fuel = fuel + 1
                new_money = money + oil_price[city]
                if new_money < expenses[city][new_fuel]:
                    expenses[city][new_fuel] = new_money
                    heapq.heappush(heap, Node(city, new_fuel, new_money))
            
            # 选项2：前往相邻城市
            for next_city, d in adj[city]:
                if fuel >= d:
                    new_fuel = fuel - d
                    if money < expenses[next_city][new_fuel]:
                        expenses[next_city][new_fuel] = money
                        heapq.heappush(heap, Node(next_city, new_fuel, money))
        
        # 如果没有找到路径
        if not found:
            print("impossible")

if __name__ == "__main__":
    main()