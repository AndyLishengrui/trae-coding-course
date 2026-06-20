#include <bits/stdc++.h>
using namespace std;

priority_queue<int, vector<int>, greater<int> > q;
int N;

int main() {
  scanf("%d", &N);
  for (int a = 1; a <= N; a++) {
    int t;
    scanf("%d", &t);
    q.push(t);
  }
  int ans = 0;
  while (q.size() > 1) {
    int l, r;
    l = q.top();
    q.pop();
    r = q.top();
    q.pop();
    ans += l + r;
    q.push(l + r);
  }
  printf("%d\n", ans);

  return 0;
}