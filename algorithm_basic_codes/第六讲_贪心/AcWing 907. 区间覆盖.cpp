#include <iostream>
#include <cstring>
#include <algorithm>

using namespace std;

const int N = 100007;

pair<int,int> range[N];
int n;

int main()
{
    int start,end;
    cin>>start>>end;
    cin>>n;
    for (int i = 0; i < n; i ++ )
    {
      int l,r;
      cin>>l>>r;
      range[i] = {l,r};
    }
    sort(range,range+n);//排序

    int res = 0;
    bool success = false;
    for (int i = 0; i < n; i ++ )
    {

      int j = i, r = -2e9;
      while(j<n && range[j].first <= start)
      {
        r =max(r,range[j].second); 
        j++;
      }

      if (r < start)
      {
        res = -1;
        break;
      }

      res++;
      if (r >= end)
      {
        success = true;
        break;
      }

      start = r;
      i = j-1;
    }

    if (!success) res = -1;
    cout<<res<<endl;

    return 0;
}