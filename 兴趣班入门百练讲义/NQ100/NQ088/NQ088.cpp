// NQ088 拦截雷电箭
#include <algorithm>
#include <iostream>
#include <vector>
using namespace std;

vector<int> s, d;  //用vector来改写代码
int main() {
  int n, h;
  cin >> n;
  //读入雷电箭,存储到vector中
  for (int i = 0; i < n; i++) {  //下标从1开始到n
    cin >> h;
    s.push_back(h);  // s[i]为终点的最长子序列
    d.push_back(1);  // d[i]初始值为1
  }
  // d[0]=1;
  //每次求以第i个数为终点的最长不上升子序列的长度
  for (int i = 1; i < n; i++)
    for (int j = 0; j < i; j++)
      //察看以第j个数为终点的最长不上升子序列
      if (s[i] <= s[j])  //比较是否不大于
        d[i] = max(d[i], d[j] + 1);
  cout << *max_element(d.begin(), d.end());  //取最大值

  return 0;
}