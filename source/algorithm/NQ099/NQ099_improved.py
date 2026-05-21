# NQ099 最省赛程 - 改进版
# Python 3.5 兼容
import heapq

MAX_N = 1010
MAX_CAPACITY = 107

def main():
    import sys
    input = sys.stdin.read().split()
    idx = 0
    
    n = int(input[idx])
    idx += 1
    m = int(input[idx])
    idx += 1
    
    oil_price = [0] * n
    for i in range(n):
        oil_price[i] = int(input[idx])
        idx += 1
    
    # 构建邻接表
    adj = [[] for _ in range(n)]
    for _ in range(m):
        u = int(input[idx])
        idx += 1
        v = int(input[idx])
        idx += 1
        d = int(input[idx])
        idx += 1
        adj[u].append((v, d))
        adj[v].append((u, d))
    
    q = int(input[idx])
    idx += 1
    
    for _ in range(q):
        c = int(input[idx])
        idx += 1
        s = int(input[idx])
        idx += 1
        e = int(input[idx])
        idx += 1
        
        # 初始化 expenses 数组
        expenses = [[float('inf')] * (c + 1) for _ in range(n)]
        visited = [[False] * (c + 1) for _ in range(n)]
        
        # 优先队列，元素为 (money, city, fuel)
        heap = []
        expenses[s][0] = 0
        heapq.heappush(heap, (0, s, 0))
        
        found = False
        result = -1
        
        while heap:
            current_money, city, fuel = heapq.heappop(heap)
            
            if city == e:
                result = current_money
                found = True
                break
            
            if visited[city][fuel]:
                continue
            visited[city][fuel] = True
            
            # 尝试加一升油
            if fuel < c:
                new_fuel = fuel + 1
                new_money = current_money + oil_price[city]
                if new_money < expenses[city][new_fuel]:
                    expenses[city][new_fuel] = new_money
                    heapq.heappush(heap, (new_money, city, new_fuel))
            
            # 尝试前往相邻城市
            for (next_city, required_fuel) in adj[city]:
                if fuel >= required_fuel:
                    new_fuel = fuel - required_fuel
                    if current_money < expenses[next_city][new_fuel]:
                        expenses[next_city][new_fuel] = current_money
                        heapq.heappush(heap, (current_money, next_city, new_fuel))
        
        if found:
            print(result)
        else:
            print("impossible")

if __name__ == "__main__":
    main()