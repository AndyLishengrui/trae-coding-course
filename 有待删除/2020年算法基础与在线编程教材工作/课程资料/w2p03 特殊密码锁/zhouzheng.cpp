#include <bits/stdc++.h>
using namespace std;

void change(bitset<50> &s, int pos) {
  if (pos) s[pos - 1] = !s[pos - 1];
  s[pos] = !s[pos];
  s[pos + 1] = !s[pos + 1];
}

int main() {
  
  cin.tie(0)->sync_with_stdio(0);  
  cout.tie(0);

  string s1, s2;
  cin >> s1 >> s2;
  int n = s1.size(), ans = n + 1;
  bitset<50> a(0), b(0);
  for (int i = 0; i < n; ++i) 
    a[i] = s1.at(i) == '1', b[i] = s2.at(i) == '1';

  int res = 0;
  for (int i = 0; i < n - 1; ++i)
    if (a[i] != b[i]) change(a, i + 1), ++res;

  a[n] = 0;
  if (a == b) ans = min(ans, res);

  for (int i = 0; i < n; ++i) 
    a[i] = s1.at(i) == '1';
  
  res = 1;
  change(a, 0);
  
  for (int i = 0; i < n - 1; ++i)
    if (a[i] != b[i]) change(a, i + 1), ++res;
  
  a[n] = 0;
  
  if (a == b) ans = min(ans, res);
  
  if (ans > n)
    puts("impossible");
  else
    printf("%d\n", ans);
  return 0;
}