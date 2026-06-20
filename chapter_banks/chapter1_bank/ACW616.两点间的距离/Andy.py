# NQ1-07: 两点间的距离
# 计算平面两点 P1(x1,y1) 和 P2(x2,y2) 的欧几里得距离，保留4位小数。

import math

x1, y1, x2, y2 = map(float, input().split())
distance = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
print(f"{distance:.4f}")
