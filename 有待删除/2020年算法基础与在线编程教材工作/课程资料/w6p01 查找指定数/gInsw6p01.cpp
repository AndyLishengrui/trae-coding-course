
#include <bits/stdc++.h>

#define For(a, begin, end) for (register int a = begin; a < end; ++a)
#define Clear(a, b) memset(a, b, sizeof(a))
using namespace std;
template <typename AAA>
inline void CMax(AAA &u, AAA v) {
  if (v > u) u = v;
}  //把最大值存在u里面

int random(int n) { return (long long)rand() * rand() % n; }
int NoZeroRandom(int n) {
  int result = random(n);
  while (result == 0) result = random(n);
  return result;
}

int randNM() {
  int n = random(100000) + 1;
  int m = 1000000000;

  for (int i = 1; i <= n; i++) {
    cout << random(2 * m + 1) - m << endl;
  }
}

int randRangeLR(int n, int m) {
  for (int i = 1; i <= m; i++) {
    int l = random(n) + 1;
    int r = random(n) + 1;
    if (l > r) swap(l, r);
    printf("%d %d\n", l, r);
  }
}
char randChar() { return char('a' + random(26)); }

int randTree(int n) {
  for (int i = 2; i <= n; i++) {
    int fa = random(i - 1) + 1;
    int val = random(1000000000) + 1;
    printf("%d %d %d\n", fa, i, val);
  }
}

const int NUM = 10;

string getname(int i, string a) {
  stringstream ss;
  ss << i << a;
  return ss.str();
}
void printGrid2str(int lines) {
  string readstr;
  For(i, 0, lines) {
    string s;
    cin >> s;
    cout << s << endl;
  }
}
vector<int> p;
int main() {
  srand((unsigned)time(0));
  //    freopen("test.in","r",stdin);
  //  弱数据
  For(t, 1, 11) {
    string inFileName;
    inFileName = getname(t, ".in");
    freopen(inFileName.c_str(), "w", stdout);

    int n = NoZeroRandom(100);  // n个数 -10000到10000之间
   
    p.resize(n);
    for (int i = 0; i < n; i++) {
      p.push_back( NoZeroRandom(1000) );
    }
    sort(p.begin(), p.end());
    p.erase(unique(p.begin(), p.end()), p.end());  //去重
    cout << p.size() << endl;
    for (auto x:p) cout <<x << " ";

    cout << endl;
    int T = NoZeroRandom(100);  // T组询问
    cout << T << endl;
    for (int i = 1; i <= T; i++) {
      cout << NoZeroRandom(1000) << endl;
    }
  }

  //  强数据
  For(t, 11, 21) {
    string inFileName;
    inFileName = getname(t, ".in");
    freopen(inFileName.c_str(), "w", stdout);

    int n = NoZeroRandom(10000);  // n个数 -10000到10000之间
    p.resize(n);
    for (int i = 0; i < n; i++) {
      p.push_back( NoZeroRandom(1000) );
    }
    sort(p.begin(), p.end());
    p.erase(unique(p.begin(), p.end()), p.end());  //去重
    cout << p.size() << endl;
    for (auto x:p) cout <<x << " ";
    cout << endl;
    int T = NoZeroRandom(10000);  // T组询问
    cout << T << endl;
    for (int i = 1; i <= T; i++) {
      cout << NoZeroRandom(100000)  << endl;
    }
  }
  return 0;
}
