#include <algorithm>
#include <cmath>
#include <iostream>
using namespace std;
const int N = 100007;
int n;
int numbers[N], tmp[N];  // tmp为临时数组用于2路归并

void mergeSort(int nums[], int left, int right) {
  if (left >= right) return;
  // 1. 确定分界点
  int mid = left + right >> 1;

  // 2. 分治左区间 [left, mid],右区间[mid+1, right]
  mergeSort(nums, left, mid), mergeSort(nums, mid + 1, right);

  // 3. 合二为一
  int k = 0, p = left, q = mid + 1;  // p,q指向左右两部分数组的起点
  //扫描还未抵达终点
  while (p <= mid && q <= right)
    if (nums[p] <= nums[q])  //把小的放到tmp数组里面
      tmp[k++] = nums[p++];
    else
      tmp[k++] = nums[q++];
  //把左边剩余的部分插入tmp
  while (p <= mid) tmp[k++] = nums[p++];
  //把右边剩余的部分插入tmp
  while (q <= right) tmp[k++] = nums[q++];
  //把tmp的部分复制回数组
  for (int i = left, k = 0; i <= right; i++, k++) nums[i] = tmp[k];
}
int main() {
  //数据大，使用printf和scanf
  scanf("%d", &n);
  for (int i = 0; i < n; i++) scanf("%d", &numbers[i]);

  mergeSort(numbers, 0, n - 1);

  for (int i = 0; i < n; i++) printf("%d ", numbers[i]);

  return 0;
}
