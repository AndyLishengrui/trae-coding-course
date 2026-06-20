#include <algorithm>
#include <cmath>
#include <iostream>
using namespace std;

typedef long long LL;  //使用long long防止溢出
const int N = 100007;
int n;
int numbers[N], tmp[N];
//最大的数可能会是 n^2/2
LL mergeSort(int nums[], int left, int right) {
  //如果左指针越过右指针，则返回
  if (left >= right) return 0;
  //确定区间端点
  int mid = left + right >> 1;
  //递归求左右两部分的逆序对数
  LL result = mergeSort(nums, left, mid) + mergeSort(nums, mid + 1, right);

  //合二为一的过程中计算逆序对个数
  int k = 0, p = left, q = mid + 1;  //左右两部分数组的起点

  while (p <= mid && q <= right)  //扫描还未抵达终点
    if (nums[p] <= nums[q])       //把小的放到tmp数组里面
      tmp[k++] = nums[p++];
    else {
      //计算逆序对的个数mid-p+1
      result += mid - p + 1;
      tmp[k++] = nums[q++];
    }

  while (p <= mid) tmp[k++] = nums[p++];    //把左边剩余的部分插入tmp
  while (q <= right) tmp[k++] = nums[q++];  //把右边剩余的部分插入tmp

  //把tmp的部分复制回数组
  for (int i = left, k = 0; i <= right; i++, k++) nums[i] = tmp[k];

  return result;
}
int main() {
  //数据大，使用printf和scanf
  scanf("%d", &n);
  
  for (int i = 0; i < n; i++) scanf("%d", &numbers[i]);

  cout << mergeSort(numbers, 0, n - 1) << endl;

  return 0;
}
