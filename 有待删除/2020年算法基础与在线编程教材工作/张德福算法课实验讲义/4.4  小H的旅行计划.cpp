#include <algorithm>
#include <cstdio>
#include <iostream>
#include <vector>
using namespace std;
int n, cw, bestw;
int dis[10][10];
int x[10], bestx[10];
const int MAX = 3e10;
void dfs(int i) {
  if (i == n - 1) {
    if (dis[x[n - 2]][x[n - 1]] != MAX && dis[x[n - 1]][x[n]] != MAX)
      if (cw + dis[x[n - 2]][x[n - 1]] + dis[x[n - 1]][x[n]] < bestw) {
        bestw = cw + dis[x[n - 2]][x[n - 1]] + dis[x[n - 1]][x[n]];  
        for (int j = 1; j <= n; j++) bestx[j] = x[j];
      }
  } else {
    for (int j = i; j < n; j++)
      if (dis[x[i - 1]][x[j]] != MAX && cw + dis[x[i - 1]][x[j]] < bestw) {
        swap(x[i], x[j]);
        cw = cw + dis[x[i - 1]][x[i]];
        dfs(i + 1);
        cw = cw - dis[x[i - 1]][x[i]];
        swap(x[i], x[j]);
      }
  }
}

int main() {
  cin >> n;
  for (int i = 1; i <= n; i++) {
    x[i] = i;
    for (int j = 1; j <= n; j++) cin >> dis[i][j];
  }
  bestw = MAX;
  cw = 0;
  dfs(2);
  cout << bestw;
  return 0;
}