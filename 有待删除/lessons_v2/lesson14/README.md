# 第14课：图论入门

> **课时：** 2小时 | **题目：** 8题（3例题+5练习） | **阶段：** 算法进阶 | **NQ138-NQ145**

## 一、教学目标

1. 图的存储：邻接矩阵 vs 邻接表（`defaultdict(list)`）
2. 拓扑排序：Kahn BFS 算法
3. 理解 Dijkstra / spfa / Floyd 三种最短路的适用场景
4. 最小生成树的两种视角：加点（Prim）vs 加边（Kruskal）

## 二、核心算法速查

| 算法 | 用途 | 复杂度 | 核心数据结构 | Python工具 |
|------|------|--------|-------------|-----------|
| 拓扑排序 | DAG排序 | O(n+m) | indegree数组 | `deque` |
| Dijkstra | 单源最短路 | O(mlogn) | dist+visited | `heapq` ★ |
| spfa | 带负权/判负环 | O(km)~O(nm) | 队列 | `deque` |
| Floyd | 多源最短路 | O(n³) | 三重循环 | — |
| Prim | MST加点 | O(n²)/O(mlogn) | 距离数组 | `heapq` |
| Kruskal | MST加边 | O(mlogm) | 并查集 | `sort`+并查集 |

### Dijkstra 堆优化核心

```python
import heapq
heap = [(0, start)]  # (距离, 节点)
dist = {start: 0}
while heap:
    d, u = heapq.heappop(heap)
    if d > dist[u]: continue  # 懒删除
    for v, w in g[u]:
        if dist.get(v, inf) > d + w:
            dist[v] = d + w
            heapq.heappush(heap, (dist[v], v))
```

### 算法直觉

- **Dijkstra：** 每次选最近的未访问点扩展，类似 BFS 但边有权重
- **Floyd：** 尝试每个点作为中间点 `k`，更新所有 i→j 经过 k 的路径
- **Prim：** 维护一个"已选集合"，每次从集合外选最近的点加入
- **Kruskal：** 贪心选最小边，并查集判环

## 三、题目列表

| # | NQ# | 题目 | AcWing | 类型 | 算法 |
|---|-----|------|--------|------|------|
| 1 | NQ138 | 拓扑序列 | 848 | 例题 | Kahn BFS |
| 2 | NQ139 | Dijkstra I | 849 | 例题 | 朴素O(n²) |
| 3 | NQ140 | Dijkstra II | 850 | 例题 | 堆优化+heapq ★ |
| 4 | NQ141 | spfa求最短路 | 851 | 练习 | spfa |
| 5 | NQ142 | Floyd | 854 | 练习 | 三重循环 |
| 6 | NQ143 | Prim | 858 | 练习 | 加点MST |
| 7 | NQ144 | Kruskal | 859 | 练习 | 加边MST+并查集 |
| 8 | NQ145 | 染色法二分图 | 860 | 练习 | 二染色判定 |

**代码文件：** `codes/nq138_acw848.cpp` ～ `codes/nq145_acw860.cpp`
