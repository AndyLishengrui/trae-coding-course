from collections import deque

def main():
    import sys
    data = list(map(int, sys.stdin.read().split()))
    idx = 0
    n = data[idx]; idx += 1
    m = data[idx]; idx += 1
    
    # 邻接表和入度数组
    adj = [[] for _ in range(n + 1)]
    in_deg = [0] * (n + 1)
    
    # 建图
    for _ in range(m):
        x = data[idx]; idx += 1
        y = data[idx]; idx += 1
        adj[x].append(y)
        in_deg[y] += 1
    
    # 拓扑排序
    q = deque()
    topo = []
    for i in range(1, n + 1):
        if in_deg[i] == 0:
            q.append(i)
    
    while q:
        u = q.popleft()
        topo.append(u)
        for v in adj[u]:
            in_deg[v] -= 1
            if in_deg[v] == 0:
                q.append(v)
    
    # 逆序计算可达节点
    reach = [set() for _ in range(n + 1)]
    for u in reversed(topo):
        reach[u].add(u)  # 节点自身可达
        for v in adj[u]:
            reach[u].update(reach[v])  # 合并邻接点的可达集合
    
    # 输出结果
    for i in range(1, n + 1):
        print(len(reach[i]))

if __name__ == "__main__":
    main()