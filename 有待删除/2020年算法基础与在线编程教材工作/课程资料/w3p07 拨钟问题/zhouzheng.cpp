// code by melacau
#include <bits/stdc++.h>

using namespace std;

const string S[] = {"ABDE", "ABC",  "BCEF", "ADG", "BDEFH",
                    "CFI",  "DEGH", "GHI",  "EFHI"};

int s[9], DP[1 << 18][10];

bool vis[1 << 18];

int main() {
  for (int i = 0; i < 9; ++i) {
    int state = 0;
    for (auto c : S[i]) state |= 1 << (c - 'A');
    s[i] = state;
  }
  int state = 0;
  for (int i = 0, x; i < 9; ++i) {
    cin >> x;
    state |= x << (i << 1);
  }
  vis[state] = 1;
  queue<int> q;
  for (q.push(state); !q.empty(); q.pop()) {
    state = q.front();
    for (int i = 0; i < 9; ++i) {
      int newState = state;
      for (int k = 0; k < 9; ++k)
        if (s[i] >> k & 1) {
          if ((state >> (k << 1) & 3) == 3)
            newState ^= 3 << (k << 1);
          else
            newState += 1 << (k << 1);
        }
      if (!vis[newState]) {
        vis[newState] = 1;
        for (int k = 0; k < 9; ++k) DP[newState][k] = DP[state][k] + (k == i);
        q.push(newState);
        if (newState == 0) break;
      }
    }
  }
  for (int i = 0; i < 9; ++i)
    for (int j = 1; j <= DP[0][i]; ++j) cout << (i + 1) << ' ';
}