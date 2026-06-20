#include <algorithm>
#include <iostream>
using namespace std;
//数据规模较大
const int N = 100010;
int q[N];  //全局数组

void quick_sort(int q[], int l, int r, int k) {
  //递归终止：左指针与右指针重叠或者越过
  if (l >= r) return;
  //左右指针为两边界之前的位置，分区点x取区间上取整的中点
  int i = l - 1, j = r + 1, x = q[l+r+1>>1];

  while (i < j) {
    do i++; while (q[i] < x);  //移动左指针
    do j--; while (q[j] > x);  //移动右指针
    if (i < j) swap(q[i], q[j]);  //交换
  }
  //判断右边分支个数是否是k个，以i为分界点
  int sr = r - i + 1;   //右区间长度为SL= r - i + 1
  if (sr == k) return;  //找到k个最大数，都移动到右区间
  if (sr > k)
    return quick_sort(q, i , r, k);  //在右区间[i,r]中继续找k个数
  else
    return quick_sort(q, l, i - 1, k - sr);  //在左区间[l, i-1]找k-sr个数
}

int main() {
  int n, k;
  scanf("%d", &n);
  //使用scanf比较快
  for (int i = 0; i < n; i++) scanf("%d", &q[i]);
  scanf("%d", &k);
  //快速选择算法，把k个最大元素移动到区间右边
  quick_sort(q, 0, n - 1, k);
  //对最后k个元素排序
  sort(q + n - k, q + n);
  //输出后k个数
  for (int j = 0; j < k; j++) cout << q[n - j - 1] << endl;
  return 0;
}