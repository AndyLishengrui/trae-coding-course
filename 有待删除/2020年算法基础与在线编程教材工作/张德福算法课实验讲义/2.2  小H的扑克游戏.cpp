#include <bits/stdc++.h>
using namespace std;

int N;
int s[1010], t[1010];

int main() {

  while (cin >> N) {
    int ans = 0;
    for (int a = 1; a <= N; a++) cin >> s[a];
    for (int a = 1; a <= N; a++) cin >> t[a];
    sort(s + 1, s + 1 + N);
    sort(t + 1, t + 1 + N);

    int sh = 1, th = 1, st = N, tt = N;
    for (int ttt = 1; ttt <= N; ttt++) {
      if (s[sh] > t[th]) {
        ans += 10;
        sh++, th++;
      } else if (s[st] > t[tt]) {
        ans += 10;
        st--, tt--;
      } else {
        if (s[sh] < t[tt]) ans -= 10;
        sh++;
        tt--;
      }
    }
    cout << ans << endl;
  }

  return 0;
}