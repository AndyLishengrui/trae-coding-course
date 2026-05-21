//NQ022竞选投票
#include <algorithm>
#include <iostream>
using namespace std;

int main() {
  int n;
  cin >> n;
  int x;
  vector<int> students;
  for (int i = 0; i < n; i++) {
    cin >> x;
    students.push_back(x / 2 + 1);  //每个班级只需要过半的人
  }
  sort(students.begin(), students.end());  //排序
  n = n / 2 + 1;                           //取前半班级
  int res = 0;
  for (int i = 0; i < n; i++) res += students[i];
  //输出结果
  cout << res << endl;
  return 0;
}