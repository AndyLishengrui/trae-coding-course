# 第14课：图论入门

> **课时：** 2小时 | **题目：** 3例题 + 3练习 | **难度：** ⭐⭐⭐⭐

## 一、本课目标
1. 掌握图的两种存储方式：邻接矩阵 vs 邻接表
2. 理解拓扑排序（BFS Kahn算法）
3. 掌握 Dijkstra、Floyd、Prim、Kruskal 四大经典算法

## 二、Python 图存储

```python
# 邻接表（推荐）
from collections import defaultdict
g = defaultdict(list)
g[u].append((v, w))  # u→v 权重w

# 邻接矩阵
INF = float('inf')
g = [[INF]*n for _ in range(n)]
```

## 三、核心算法速查

| 算法 | 用途 | 复杂度 | Python关键工具 |
|------|------|--------|---------------|
| 拓扑排序 | DAG排序 | O(n+m) | `deque`+入度数组 |
| Dijkstra | 单源最短路（非负权） | O(mlogn) | `heapq` |
| Floyd | 多源最短路 | O(n³) | 三重循环 |
| Prim | 最小生成树 | O(n²)/O(mlogn) | `heapq` |
| Kruskal | 最小生成树 | O(mlogm) | `sort`+并查集 |

## 四、题目

| 题号 | 题目 | 类型 | 算法 |
|------|------|------|------|
| NQ079 | 拓扑序列 | 例题 | 拓扑排序 |
| NQ080 | Dijkstra I | 例题 | 朴素Dijkstra O(n²) |
| NQ081 | Dijkstra II | 例题 | 堆优化+`heapq` |
| NQ082 | Floyd | 练习 | 三重循环 |
| NQ083 | Prim | 练习 | `heapq`优化 |
| NQ084 | Kruskal | 练习 | 排序+并查集 |

## 五、AI 协作要点

图论算法名字多、看起来吓人。教学的要点是让学生理解核心直觉：
- Dijkstra: 每次选最近的未访问点扩展
- Floyd: 尝试每个点作为中间点
- Prim: 从集合出发找最近的外部点
- Kruskal: 贪心地选最小的不形成环的边
