# 拓扑排序算法（Kahn算法 - BFS实现）
# 用于解决有向无环图(DAG)的拓扑排序问题
import sys
from collections import deque

def main():
    # 读取输入数据
    data = sys.stdin.read().split()
    idx = 0
    n = int(data[idx]); idx += 1  # 节点数
    m = int(data[idx]); idx += 1  # 边数
    
    # 构建邻接表和入度数组
    adj = [[] for _ in range(n+1)]  # 邻接表
    in_deg = [0] * (n+1)  # 入度数组
    
    # 读取边信息并构建图
    for _ in range(m):
        a = int(data[idx]); idx += 1
        b = int(data[idx]); idx += 1
        adj[a].append(b)  # 添加边 a -> b
        in_deg[b] += 1  # 更新节点b的入度
    
    # 初始化队列，将所有入度为0的节点加入队列
    q = deque()
    for i in range(1, n+1):
        if in_deg[i] == 0:
            q.append(i)
    
    # 执行拓扑排序
    topo = []
    while q:
        u = q.popleft()  # 取出入度为0的节点
        topo.append(u)   # 将节点加入拓扑序列
        
        # 遍历当前节点的所有邻接节点
        for v in adj[u]:
            in_deg[v] -= 1  # 减少邻接节点的入度
            if in_deg[v] == 0:  # 如果邻接节点入度变为0，加入队列
                q.append(v)
    
    # 检查是否存在环
    if len(topo) == n:
        print(' '.join(map(str, topo)))
    else:
        print(-1)  # 存在环，无法拓扑排序

if __name__ == "__main__":
    main()