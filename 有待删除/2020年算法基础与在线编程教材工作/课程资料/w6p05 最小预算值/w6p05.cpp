// code by Andy 2021.04.01
#include <algorithm>
#include <iostream>
using namespace std;
int cost[100005];  //每天的实销数
int N, M;          // M为分组数
int MinCost = 1 << 32, Total = 0;

// check(mid)函数
//贪心策略：从第一个日子开始扫描，判断当前天的可否加入当前组中。
// todo 1 如果第i天的cost[i]大于x，那么说明该x太小,返回false
// todo 2 如果cost[i]+ subtotal > x，开始新的分组，否则 subtotal += cost[i]
// todo 3 如果全部处理完毕，分的组数cnt<=M, 则return true.
bool isBudgetBigEnough(int x) {
  int cnt = 1, subtotal = 0;   //当前分组的预算汇总值
  for (int i = 0; i < N; i++)  //扫描所有日子的cost值
  {
    // x太小以至于有无法归入组的日子，返回false
    if (cost[i] > x) return false;
    if (cost[i] + subtotal > x) {
      subtotal = cost[i];  //开始新的分组
      cnt++;               //分组数+1
      if (cnt > M)         //分组数大于M，返回false
        return false;
    } else {
      subtotal += cost[i];  //本组预算值累加
    }
  }
  //所有日子都扫描完毕并且cnt<=M
  return true;
}

//? 整数二分模板1
//! 左区间[l,mid], 右区间[mid+1,r]
int bsearch_1(int l, int r) {
  while (l < r) {
    int mid = l + r >> 1;
    //若一个Budge可以合法的完成M组的分割，那么需要寻找更小的可行预算。
    //因为更大的预算肯定可以分M组
    if (isBudgetBigEnough(mid))
      r = mid;  //去掉右区间，去左区间搜索
    else
      l = mid + 1;  //去掉你左区间，去右区间搜索
  }
  return l;
}

int main() {
  cin >> N >> M;  //读入N,M
  for (int i = 0; i < N; i++) {
    cin >> cost[i];
    MinCost = min(MinCost, cost[i]);  //取最小值
    Total += cost[i];                 //计算综合
  }
  cout << bsearch_1(MinCost, Total) << endl;
  return 0;
}
