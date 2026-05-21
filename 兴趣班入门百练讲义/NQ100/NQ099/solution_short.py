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
    input_lines = [line.strip() for line in sys.stdin if line.strip()]
    ptr = 0
    n, m = map(int, input_lines[ptr].split())
    ptr += 1
    oil_price = list(map(int, input_lines[ptr].split()))
    ptr += 1
    # 构建邻接表
    adj = [[] for _ in range(n)]
    for _ in range(m):
        u, v, d = map(int, input_lines[ptr].split())
        ptr += 1
        adj[u].append((v, d))
        adj[v].append((u, d))
    q = int(input_lines[ptr])
    ptr += 1
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
            if visited[city][fuel]:
                continue
            visited[city][fuel] = true
            # 如果到达终点
            if city == e:
                print(money)
                found = true
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
        if not found:
            print("impossible")
if __name__ == "__main__":
    main()