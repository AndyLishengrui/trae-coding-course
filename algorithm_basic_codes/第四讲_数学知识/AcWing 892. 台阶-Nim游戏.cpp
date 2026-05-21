//只需要考虑奇数级台阶的情况
#include <iostream>
#include <cstring>
#include <algorithm>

using namespace std;

int main()
{
    int n;
    int res = 0;
    scanf("%d", &n);
    for (int i = 1; i <= n; i++)
    {
      int x;
      scanf("%d", &x);
      if (i % 2) res ^= x;//奇数台阶的情况求异或（Nim游戏）
    }

    if (res) puts("Yes");//先手必胜
    else puts("No");//先手必败

    return 0;
}