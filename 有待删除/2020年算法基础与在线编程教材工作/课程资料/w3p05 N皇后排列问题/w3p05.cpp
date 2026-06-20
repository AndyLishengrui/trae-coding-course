#include <iostream>
#include <vector>
using namespace std;
int N;  //读入的皇后个数

// res 存储皇后的一组解
// res[0]  存储皇后第1行的位置
// res[i-1]存储皇后第i行的位置
// 皇后坐标(x,y) 为 (res[i],i)
vector<int> res;

void dfs(int n) {
  //递归出口，n从0开始到N-1全部遍历完毕
  if (n == N) {
    for (auto x : res) cout << x;
    cout << endl;
    return;
  }
  // 假定n-1个皇后已经全部摆好，现在准备摆第n个皇后
  // 意味着res[0]--res[n-1]已经有值了
  for (int i = 1; i <= N; i++)  //尝试0-N列位置，摆放第n个皇后
  {
    // 点(x1,y1)与点(x2,y2)在同一对角线上，则有|x1-x2|==|y1-y2|
    // 因此若 (i,n) 与 (res[k],k) 满足 |i-res[k]| == |n - k|
    // 则两点在同一对角线上
    int k;
    for (k = 0; k < n; k++)
      if ((res[k] == i) ||                //发现同列，跳出
          abs(i - res[k]) == abs(n - k))  //对角线，跳出
        break;
    if (k == n) {
      res[n] = i;  //把当前第n个皇后放在第i个位置上
      dfs(n + 1);
    }
  }
}
int main() {
  //全局变量N皇后
  cin >> N;
  res.resize(N);
  dfs(0);
  return 0;
}
