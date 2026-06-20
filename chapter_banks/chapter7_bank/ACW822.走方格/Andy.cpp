#include <iostream>

using namespace std;

int n, m;
int ans;

void dfs(int x, int y)
{
    if (x == n && y == m) ans ++ ;
    else
    {
      if (y < m) dfs(x, y + 1);
      if (x < n) dfs(x + 1, y);
    }
}

int main()
{
    cin >> n >> m;
    dfs(0, 0);
    cout << ans << endl;

    return 0;
}
