# 第9课：排序与二分

> **课时：** 2小时 | **题目：** 7题（4例题+3练习） | **阶段：** 核心算法 | **NQ101-NQ107**

## 一、教学目标

1. 手写快速排序和归并排序，理解**分治思想**（divide and conquer）
2. 快速选择算法：TopK 问题的 O(n) 解法
3. 整数二分和浮点二分的**模板差异**（+1 问题）
4. **库对照：** 日常用 `sort()`/`bisect`，算法理解用手写

## 二、核心模板（AcWing 模板体系）

### 快速排序

```cpp
void quick_sort(int q[], int l, int r) {
    if (l >= r) return;
    int i = l - 1, j = r + 1, x = q[l + r >> 1];
    while (i < j) {
        do i++; while (q[i] < x);
        do j--; while (q[j] > x);
        if (i < j) swap(q[i], q[j]);
    }
    quick_sort(q, l, j);
    quick_sort(q, j + 1, r);
}
```

### 整数二分（两种模板）

```cpp
// 模板1：区间[l,r] → [l,mid] + [mid+1,r]
int bsearch_1(int l, int r) {
    while (l < r) {
        int mid = l + r >> 1;
        if (check(mid)) r = mid;
        else l = mid + 1;
    }
    return l;
}

// 模板2：区间[l,r] → [l,mid-1] + [mid,r]
int bsearch_2(int l, int r) {
    while (l < r) {
        int mid = l + r + 1 >> 1;  // 注意 +1！
        if (check(mid)) l = mid;
        else r = mid - 1;
    }
    return l;
}
```

**教学点：** 模板2 的 `mid = l + r + 1 >> 1` 中 +1 是最容易出错的地方。让学生用 `l=0, r=1` 走一遍不+1的情况：`mid=0`，若 `check(0)=true` 则 `l=mid=0`，死循环。

### 浮点二分

```cpp
double bsearch(double l, double r) {
    const double eps = 1e-6;  // 精度要求
    while (r - l > eps) {
        double mid = (l + r) / 2;
        if (check(mid)) r = mid;
        else l = mid;
    }
    return l;
}
```

## 三、Python 库对标

| 需求 | C++ | Python |
|------|-----|--------|
| 排序 | `sort(begin,end)` | `arr.sort()` / `sorted(arr)` |
| 左二分 | 手写 bsearch_1 | `bisect.bisect_left(arr, x)` |
| 右二分 | 手写 bsearch_2 | `bisect.bisect_right(arr, x)` |
| nth_element | `nth_element` / 手写 | `sorted(arr)[k-1]` 或手写 quick_select |

## 四、题目列表

| # | NQ# | 题目 | AcWing | 类型 | 算法 |
|---|-----|------|--------|------|------|
| 1 | NQ101 | 快速排序 | 785 | 例题 | 快排模板 |
| 2 | NQ102 | 第k个数 | 786 | 例题 | 快速选择 |
| 3 | NQ103 | 归并排序 | 787 | 例题 | 归并模板 |
| 4 | NQ104 | 逆序对的数量 | 788 | 例题 | 归并统计 ★ |
| 5 | NQ105 | 数的范围 | 789 | 练习 | 整数二分 |
| 6 | NQ106 | 数的三次方根 | 790 | 练习 | 浮点二分 |
| 7 | NQ107 | 菱形 | 727 | 练习 | 曼哈顿距离 |

## 五、AI 协作要点

1. 排序模板不需要死记。让 Trae 生成快排代码，然后逐行标注"分区点选择"、"指针移动"、"递归终止"的含义
2. 二分模板的 +1 问题，让 Trae 用 `l=0, r=1` 推演两遍，展示死循环
3. NQ104 逆序对数量，让学生先用暴力 O(n²) 理解，再展示归并优化到 O(n log n)

**代码文件：** `codes/nq101_acw785.cpp` ～ `codes/nq107_acw727.cpp`
