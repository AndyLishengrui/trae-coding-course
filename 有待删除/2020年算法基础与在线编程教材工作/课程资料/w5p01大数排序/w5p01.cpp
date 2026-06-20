#include <iostream>

using namespace std;
//数据规模较大
const int N = 1000010;
int q[N];//全局数组

void quick_sort(int q[], int l, int r) {
  //递归终止：左指针与右指针重叠或者越过
  if (l >= r) return;
  //左右指针为两边界之前的位置，分区点x取区间中点
  int i = l - 1, j = r + 1, x = q[l + r >> 1];
  //
  while (i < j) {
    //移动左指针
    do  i++; while (q[i] < x);
    //移动右指针
    do  j--; while (q[j] > x);
    //交换
    if (i < j) swap(q[i], q[j]);
  }
  //递归处理子问题
  quick_sort(q, l, j); //左区间[l,j]
  quick_sort(q, j + 1, r); //右区间 [j+1,r]
}

int main() {
  int n;
  scanf("%d", &n);
  //使用scanf比较快
  for (int i = 0; i < n; i++) scanf("%d", &q[i]);
  //快速排序
  quick_sort(q, 0, n - 1);
  //使用printf比较快
  for (int i = 0; i < n; i++) printf("%d ", q[i]);

  return 0;
}