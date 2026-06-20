#include <algorithm>
#include <cstring>
#include <iostream>
#include <vector>
using namespace std;

vector<string> ans;
string path;
vector<bool> used;

void dfs(string s, int u) {
  //抵达最底层
  if (u == s.size()) {
    ans.push_back(path);
    return;
  }
  //! 遍历used数组，枚举下一个还没用的元素
  for (int i = 0; i < s.size(); i++)
    if (used[i] == false) {
      path[u] = s[i];  //记录当前尝试的元素
      used[i] = true;
      dfs(s, u + 1);
      used[i] = false;  //恢复现场
    }
}

int main() {
  string line;
  cin >> line;
  //初始化
  sort(line.begin(), line.end());    //排序字符串
  path = line;                       // path的长度初始化(内容无所谓)
  used = vector<bool>(line.size());  //第i位字符是否被访问的状态数组
  //递归搜索
  dfs(line, 0);
  //输出
  for (auto l : ans) cout << l << endl;
  return 0;
}

// 方法二
// #include <algorithm>
// #include <iostream>
// #include <string>
// using namespace std;

// int main() {
  
//   //输入字符串
//   string line;
//   cin >> line;
//   //排序
//   sort(line.begin(), line.end());
//   //输出最小排列
//   cout << line << endl;
//   //调用next_permutation生成下一个字典序排列
//   while (next_permutation(line.begin(), line.end())) 
//     cout << line << endl;//输出新的序列

//   return 0;
// }
