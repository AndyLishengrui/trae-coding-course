// NQ009 循环求解
#include <iostream>
using namespace std;
int main() {
  int a, b;
  while (cin >> a >> b) {
    if (a > b) swap(a, b);
    long long s1 = 0, s2 = 0;
    for (int i = a; i <= b; i++)
      if (i % 2)
        s2 += i * i * i;
      else
        s1 += i * i;
    cout << s1 << ' ' << s2 << endl;
  }
  return 0;
}