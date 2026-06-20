#include <algorithm>
#include <cmath>
#include <iomanip>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <string>
using namespace std;
int a[15] = {0};
int arr[15][15] = {0};
int sum = 0, n, b[1000], c[1000], d[1000];
void dfs(int deep) {
  if (deep == 0) {
    sum++;
    return;
  }
  for (int i = 1; i <= n; i++) {
    int l = n - deep + 1;
    if (b[i] == 0 && c[l + i] == 0 && d[l - i + n] == 0) {
      a[l] = i;
      b[i] = 1;
      c[l + i] = 1;
      d[l - i + n] = 1;
      dfs(deep - 1);
      a[l] = 0;
      b[i] = 0;
      c[l + i] = 0;
      d[l - i + n] = 0;
    }
  }
  return;
}

int main() {
  cin >> n;
  dfs(n);
  cout << sum;
  return 0;
}