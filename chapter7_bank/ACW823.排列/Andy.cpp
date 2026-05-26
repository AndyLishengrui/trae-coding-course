#include <iostream>

using namespace std;

const int N = 10;

int n;

void dfs(int u, int nums[], bool st[])
{
  if (u > n)
  {
    for (int i = 1; i <= n; i ++ ) cout << nums[i] << ' ';
    cout << endl;
  }
  else
  {
    for (int i = 1; i <= n; i ++ )
        if (!st[i])
        {
          st[i] = true;
          nums[u] = i;
          dfs(u + 1, nums, st);
          st[i] = false;
        }
  }
}

int main()
{
    cin >> n;

    int nums[N];
    bool st[N] = {0};

    dfs(1, nums, st);

    return 0;
}
