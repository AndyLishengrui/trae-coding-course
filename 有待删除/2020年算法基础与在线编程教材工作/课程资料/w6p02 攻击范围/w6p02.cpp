#include <algorithm>
#include <iostream>
using namespace std;
const int N = 100007;

int nums[N];

int main() {
  // 第一行包含整数n和q，表示数组长度和询问个数。
  int n, q; /*  */
  scanf("%d%d", &n, &q);
  // 第二行包含n个整数（均在1~10000范围内），表示完整数组。
  for (int i = 0; i < n; i++) scanf("%d", &nums[i]);
  // 接下来q行，每行包含一个整数k，表示一个询问元素。
  while (q--) {
    //读入要查找的数，并且二分查找其范围
    int k;
    scanf("%d", &k);  // 读入k
    //! 寻找左边界
    int left = 0, right = n - 1;  //初始化left和right
    while (left < right)          //模板1
    {
      int mid = left + right >> 1;  //模板1
      if (nums[mid] >= k)
        right = mid;
      else
        left = mid + 1;
    }
    // left就是左端点值
    //判断是否找得到
    if (nums[left] != k)
      cout << "-1 -1" << endl;  //找不到x
    else {
      cout << left << " ";
      //! 继续寻找右边界
      //重新初始化left,right,进行第二次二分搜索
      left = 0, right = n - 1;
      while (left < right) {
        int mid = left + right + 1 >> 1;  //模板2
        if (nums[mid] <= k)
          left = mid;
        else
          right = mid - 1;
      }
      cout << left << endl;
    }
  }

  return 0;
}

// int bsearch_1(int left, int right)
// {
//     while (left < right)
//     {
//         int mid = left + right >> 1;
//         if (check(mid)) right = mid;
//         else left = mid + 1;
//     }
//     return left;
// }

// int bsearch_2(int left, int right)
// {
//     while (left < right)
//     {
//         int mid = left + right + 1 >> 1;
//         if (check(mid)) left = mid;
//         else right = mid - 1;
//     }
//     return left;
// }