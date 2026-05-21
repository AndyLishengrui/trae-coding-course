#include <iostream>
#include <vector>

// 数组最大尺寸，N <= 100000
const int kMaxN = 100005;

// 定义全局数组，以避免在递归中反复分配内存，提高效率。
// arr 存储原始数据，temp_arr 用于归并时的临时存储空间。
int arr[kMaxN];
int temp_arr[kMaxN];

/**
 * @brief 将两个有序子序列 arr[l...mid] 和 arr[mid+1...r] 合并成一个有序序列。
 * @param a 待排序的数组
 * @param l 左边界 (left)
 * @param mid 中间点
 * @param r 右边界 (right)
 */
void Merge(int a[], int l, int mid, int r) {
    // i: 左半部分指针 (从 l 到 mid)
    // j: 右半部分指针 (从 mid+1 到 r)
    // k: 辅助数组指针 (从 l 开始填充)
    int i = l;
    int j = mid + 1;
    int k = l;

    // 1. 双指针比较，将较小元素放入 temp_arr
    while (i <= mid && j <= r) {
        if (a[i] <= a[j]) { // 稳定性体现：如果相等，优先取左侧元素
            temp_arr[k++] = a[i++];
        } else {
            temp_arr[k++] = a[j++];
        }
    }

    // 2. 处理左半部分剩余元素
    while (i <= mid) {
        temp_arr[k++] = a[i++];
    }

    // 3. 处理右半部分剩余元素
    while (j <= r) {
        temp_arr[k++] = a[j++];
    }

    // 4. 将 temp_arr 中排好序的元素复制回原数组 a[l...r]
    for (int idx = l; idx <= r; ++idx) {
        a[idx] = temp_arr[idx];
    }
}

/**
 * @brief 递归实现归并排序
 * @param a 待排序的数组
 * @param l 左边界 (left)
 * @param r 右边界 (right)
 */
void MergeSort(int a[], int l, int r) {
    // 基准情况：如果子序列长度为 0 或 1，则已经有序
    if (l >= r) {
        return;
    }
    
    // 计算中点。使用这种方式计算 mid 避免整数溢出风险 (虽然本题数据范围较小)
    int mid = l + (r - l) / 2;
    
    // 1. 递归排序左半部分
    MergeSort(a, l, mid);
    
    // 2. 递归排序右半部分
    MergeSort(a, mid + 1, r);
    
    // 3. 合并两个有序的子序列
    Merge(a, l, mid, r);
}

int main() {
    // 优化输入输出速度
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(NULL);

    int n;
    if (!(std::cin >> n)) return 0;

    // 读取 n 个整数
    for (int i = 0; i < n; ++i) {
        if (!(std::cin >> arr[i])) return 0;
    }

    // 对整个数组进行归并排序 (索引范围 0 到 n-1)
    MergeSort(arr, 0, n - 1);

    // 输出排好序的数列
    for (int i = 0; i < n; ++i) {
        std::cout << arr[i] << (i == n - 1 ? "" : " ");
    }
    std::cout << "\n";

    return 0;
}