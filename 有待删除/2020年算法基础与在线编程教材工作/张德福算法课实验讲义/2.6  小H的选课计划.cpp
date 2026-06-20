#include <bits/stdc++.h>
using namespace std;

int N, T;
int s[1000];
int m[100][100];
int du[100], ok[100];

int main() {
  cin >> T;
  while (T--) {
    cin >> N;

    memset(du, 0, sizeof(du));
    memset(m, 0, sizeof(m));
    memset(ok, 0, sizeof(ok));

    for (int a = 1; a <= N; a++) cin >> s[a];

    for (int a = 1; a <= N; a++) {
      int k;
      cin >> k;
      for (int b = 1; b <= k; b++) {
        int t;
        cin >> t;
        m[t][a] = 1;
        du[a]++;
      }
    }
    int ini = 0;
    while (1) {
      int mv = -1, mp = 0;
      for (int a = 1; a <= N; a++)
        if (du[a] == 0 && !ok[a] && mv < s[a]) {
          mv = s[a];
          mp = a;
        }
      if (mv == -1)
        break;
      else {
        if (!ini)
          ini = 1;
        else
          printf(" ");
      }
      cout << mp;
      ok[mp] = 1;
      for (int a = 1; a <= N; a++)
        if (m[mp][a] && !ok[a]) du[a]--;
    }
    cout << endl;
  }

  return 0;
}