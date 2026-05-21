#include <iostream>
#include <cstring>
#include <algorithm>

using namespace std;
typedef pair<int, int> PII;


const int N = 500007;

int n;
PII a[N];

int main()
{
    ios::sync_with_stdio(false);
    //读入数据
    cin>>n;
    for (int i = 0; i < n; i ++ )
    {
      int w, s;
      cin>>w>>s;
      a[i] = {w+s,w};
    }

    sort(a, a+n);

    int res = -1e9;
    for (int i = 0, sum = 0; i < n; i ++ )
    {
      int w = a[i].second, s = a[i].first - w;
      res = max(res, sum - s);
      sum += w;
    }

    cout<<res<<endl;
    return 0;

}