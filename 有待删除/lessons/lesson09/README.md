# 第9课：排序与二分

> **课时：** 2小时 | **题目：** 3例题 + 3练习 | **难度：** ⭐⭐⭐ | **进入算法阶段**

## 一、本课目标
1. 手写快速排序和归并排序，理解分治思想
2. 掌握快速选择算法（TopK问题）
3. 理解整数二分和浮点二分的模板差异
4. **库优先：** 日常开发用 `sort()`/`bisect`，面试/竞赛用手写模板

## 二、核心模板（来自 AcWing 模板体系）

### 快速排序模板
```cpp
void quick_sort(int q[], int l, int r) {
    if (l >= r) return;
    int i = l - 1, j = r + 1, x = q[l + r >> 1];
    while (i < j) {
        do i++; while (q[i] < x);
        do j--; while (q[j] > x);
        if (i < j) swap(q[i], q[j]);
    }
    quick_sort(q, l, j), quick_sort(q, j + 1, r);
}
```

### 整数二分模板
```cpp
// 区间[l, r]被划分成[l, mid]和[mid+1, r]
int bsearch_1(int l, int r) {
    while (l < r) {
        int mid = l + r >> 1;
        if (check(mid)) r = mid;
        else l = mid + 1;
    }
    return l;
}
```

## 三、Python 对标工具

| 需求 | C++ | Python |
|------|-----|--------|
| 排序 | `sort(begin,end)` | `arr.sort()` / `sorted(arr)` |
| 左二分 | 手写 bsearch_1 | `bisect.bisect_left(arr, x)` |
| 右二分 | 手写 bsearch_2 | `bisect.bisect_right(arr, x)` |
| 第k小数 | `nth_element` | `sorted(arr)[k-1]` 或手写 quick_select |

## 四、例题 + 练习

| 题号 | 题目 | 类型 | 核心 |
|------|------|------|------|
| NQ049 | 快速排序 | 例题 | 手写快排模板 |
| NQ050 | 第k个数 | 例题 | 快速选择 Quick Select |
| NQ051 | 归并排序 | 例题 | 手写归并模板 |
| NQ052 | 逆序对的数量 | 练习 | 归并排序统计逆序对 |
| NQ053 | 数的范围 | 练习 | 整数二分，`bisect_left/right` |
| NQ054 | 数的三次方根 | 练习 | 浮点二分 |

## 五、AI 协作要点

排序算法是理解分治思想的最佳入口。让学生先用 Trae 生成快排代码，然后跳出代码看结构："这本质上是不是把数组分成两半分别处理？" 和归并排序对比："归并是先分后合，快排是先分再各自排。"
